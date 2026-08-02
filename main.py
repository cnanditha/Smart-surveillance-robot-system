import cv2
import numpy as np
import urllib.request
from ultralytics import YOLO

# The working stream URL over your mobile hotspot
STREAM_URL = "http://10.223.238.48:81/stream"

print("Loading YOLOv8 Small model (this may take a minute to download the first time)...")
# Upgraded to the smarter 'Small' model to stop hallucinating objects
model = YOLO('yolov8s.pt')

print(f"Connecting to ESP32-CAM stream at {STREAM_URL}...")

try:
    # Open the continuous video stream
    stream = urllib.request.urlopen(STREAM_URL)
    bytes_data = bytes()
except Exception as e:
    print(f"Failed to connect to stream: {e}")
    print("Ensure the car is on, on the same hotspot, and the browser tab is closed.")
    exit()

print("Successfully connected! Press 'q' in the video window to quit.")

while True:
    try:
        # Read chunks of the live video stream
        bytes_data += stream.read(4096)
        
        # Find the start and end markers of a single JPEG frame
        a = bytes_data.find(b'\xff\xd8') # JPEG start
        b = bytes_data.find(b'\xff\xd9') # JPEG end
        
        if a != -1 and b != -1:
            # Ensure the start marker comes BEFORE the end marker
            if a < b:
                jpg = bytes_data[a:b+2]
                bytes_data = bytes_data[b+2:] # Clear buffer for next frame
                
                # SAFETY NET: Only decode if the image actually has data
                if len(jpg) > 0:
                    frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    
                    if frame is not None:
                        # Run YOLO object detection with the stricter confidence score
                        results = model(frame, conf=0.65)
                        
                        # Draw the bounding boxes and labels
                        annotated_frame = results[0].plot()
                        
                        # Display the live video feed
                        cv2.imshow("ESP32-CAM Object Detection", annotated_frame)
                        
                        # Listen for the 'q' key to quit
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
            else:
                # If the packet got scrambled over Wi-Fi, drop it and reset
                bytes_data = bytes_data[a:]
                
    except Exception as e:
        # If anything else fails, don't crash, just keep going!
        continue

cv2.destroyAllWindows()