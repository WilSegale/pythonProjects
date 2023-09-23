from DontEdit import *
# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the grayscale frame
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Canny edge detector to find edges in the blurred frame
    edges = cv2.Canny(gray, 10, 70)

    # Invert the edges to create a sketch-like effect
    edges = cv2.bitwise_not(edges)

    # Display the sketch on the screen
    cv2.imshow("Sketch", edges)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()
