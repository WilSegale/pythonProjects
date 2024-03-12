import cv2

def main():
    try:
        # Open the default camera (usually the first camera connected to the system)
        cap = cv2.VideoCapture(0)

        # Check if the camera was opened successfully
        if not cap.isOpened():
            print("Error: Couldn't open camera.")
            return

        # Loop to continuously read frames from the camera
        while True:
            # Read a frame from the cameras
            ret, frame = cap.read()

            # Check if the frame was read successfully
            if not ret:
                print("Error: Couldn't read frame.")
                break

            # Display the frame
            cv2.imshow("Camera", frame)

            # Check for key press, if 'q' is pressed, exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting loop")
                break

    except KeyboardInterrupt:
        exit()
    finally:
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
