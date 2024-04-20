import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Video Capture with OpenCV")

    # Use device index 1 for the external camera
    cap = cv2.VideoCapture(1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open camera")
        return

    frame_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.write("The video capture has ended.")
            break

        # Display the frame
        frame_placeholder.image(frame, channels="BGR")

        # Check for the 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
