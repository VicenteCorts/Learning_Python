import cv2
import mediapipe as mp
import math

class FingerCounter:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def count_fingers(self, frame):
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect hands
        results = self.hands.process(rgb_frame)
        
        # Initialize finger count
        finger_count = 0
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS
                )
                
                # Finger tip and base landmarks for each finger
                tip_ids = [
                    self.mp_hands.HandLandmark.THUMB_TIP,
                    self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
                    self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                    self.mp_hands.HandLandmark.RING_FINGER_TIP,
                    self.mp_hands.HandLandmark.PINKY_TIP
                ]
                
                base_ids = [
                    self.mp_hands.HandLandmark.THUMB_MCP,
                    self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                    self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                    self.mp_hands.HandLandmark.RING_FINGER_MCP,
                    self.mp_hands.HandLandmark.PINKY_MCP
                ]
                
                # Check each finger
                for i in range(1, 5):  # Exclude thumb initially
                    tip = hand_landmarks.landmark[tip_ids[i]]
                    base = hand_landmarks.landmark[base_ids[i]]
                    
                    # Check if finger is raised
                    if tip.y < base.y:
                        finger_count += 1
                
                # Special check for thumb (different logic)
                thumb_tip = hand_landmarks.landmark[tip_ids[0]]
                thumb_mcp = hand_landmarks.landmark[base_ids[0]]
                
                # Check thumb position based on hand orientation
                if thumb_tip.x < thumb_mcp.x:
                    finger_count += 1
        
        return finger_count

def main():
    # Open webcam
    cap = cv2.VideoCapture(0)
    
    # Create FingerCounter instance
    finger_counter = FingerCounter()
    
    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Count fingers
        finger_count = finger_counter.count_fingers(frame)
        
        # Display finger count
        cv2.putText(
            frame, 
            f'Fingers: {finger_count}', 
            (10, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 0), 
            2
        )
        
        # Show the frame
        cv2.imshow('Finger Counter', frame)
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()