import cv2
import streamlit as st
import numpy as np

# Custom class to maintain session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

def main():
    st.title("Video Capture with OpenCV")

    # Create a session state object
    session_state = SessionState(stop_button_pressed=False)

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open webcam")
        return

    frame_placeholder = st.empty()

    while cap.isOpened() and not session_state.stop_button_pressed:
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
