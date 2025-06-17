import numpy as np
import cv2
import mediapipe as mp
import math
import pyautogui


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open Camera
capture = cv2.VideoCapture(0)

while capture.isOpened():

    # Capture frames from the camera
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    result = hands.process(rgb_frame)

    # Add logging and visual feedback for debugging
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            try:
                # Extract landmark positions for gesture recognition
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                # Adjust thresholds dynamically based on hand position
                thumb_threshold = max(0.5, thumb_tip.y - 0.1)
                pinky_threshold = max(0.5, pinky_tip.y - 0.1)

                # Display landmark positions for debugging
                cv2.putText(frame, f"Thumb: {thumb_tip.y:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, f"Pinky: {pinky_tip.y:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                # Define "jump" gesture: Both hands raised (e.g., thumb and pinky above a threshold)
                if thumb_tip.y < thumb_threshold and pinky_tip.y < pinky_threshold:
                    pyautogui.press('space')
                    cv2.putText(frame, "JUMP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "No Jump", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            except Exception as e:
                # Handle cases where landmarks are missing or hand is folded
                cv2.putText(frame, "Gesture not detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                print(f"Error processing landmarks: {e}")
    else:
        # Timeout mechanism to prevent prolonged processing
        cv2.putText(frame, "No hands detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Gesture", frame)

    # Close the camera if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
hands.close()
cv2.destroyAllWindows()