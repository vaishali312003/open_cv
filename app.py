import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Video Capture with OpenCV")

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open webcam")
        return

    stop_button_pressed = st.button("Stop")
    frame_placeholder = st.empty()

    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()

        if not ret:
            st.write("The video capture has ended.")
            break

        # Display the frame
        frame_placeholder.image(frame, channels="BGR")

        # Check for the 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
