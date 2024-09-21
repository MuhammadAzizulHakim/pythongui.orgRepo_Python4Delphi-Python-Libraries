import cv2

# Capture video from file
cap = cv2.VideoCapture('C:/Users/ASUS/OpenCV+ChatGPT/5158727-sd_640_360_30fps.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Read until the video is completed
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()
