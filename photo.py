import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Couldn't open the webcam")
    exit()

# Capture a frame from the webcam
ret, frame = cap.read()

# Check if the frame is captured correctly
if not ret:
    print("Error: Couldn't capture frame")
    exit()

# Save the captured frame as an image
cv2.imwrite("captured_photo.jpg", frame)

# Release the webcam
cap.release()

# Print a message to indicate the photo is captured
print("Photo captured successfully!")

# Display the captured photo
cv2.imshow("Captured Photo", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
