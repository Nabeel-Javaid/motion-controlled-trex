#!/usr/bin/env python3
"""
Test script for gesture detection
This script demonstrates the gesture detection without needing the browser game
"""

import cv2
import mediapipe as mp
import numpy as np
import time
from typing import List, Tuple

class GestureDemo:
    def __init__(self):
        # Initialize MediaPipe hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Gesture detection variables
        self.prev_index_up = False
        self.jump_count = 0
        
        print("🦕 Gesture Detection Demo")
        print("👋 Show your hand to the camera")
        print("☝️  Lift your index finger to trigger 'jump' detection!")
        print("❌ Press 'q' to quit")

    def get_finger_landmarks(self, hand_landmarks) -> List[Tuple[float, float]]:
        """Extract finger tip and joint positions"""
        # MediaPipe hand landmark indices
        FINGER_TIPS = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky tips
        FINGER_PIPS = [3, 6, 10, 14, 18]  # Finger joints (PIP joints)
        
        tips = []
        pips = []
        
        for tip_id, pip_id in zip(FINGER_TIPS, FINGER_PIPS):
            tip = hand_landmarks.landmark[tip_id]
            pip = hand_landmarks.landmark[pip_id]
            tips.append((tip.x, tip.y))
            pips.append((pip.x, pip.y))
        
        return tips, pips

    def is_index_finger_up(self, tips: List[Tuple[float, float]], pips: List[Tuple[float, float]]) -> bool:
        """Check if index finger is extended (up)"""
        # Index finger is at index 1 (tips[1], pips[1])
        index_tip_y = tips[1][1]
        index_pip_y = pips[1][1]
        
        # Check if index finger tip is above its PIP joint (lower y value = higher in image)
        index_up = index_tip_y < index_pip_y - 0.05  # Add some threshold
        
        return index_up

    def detect_jump_gesture(self, hand_landmarks) -> bool:
        """Detect if user is making a jump gesture (index finger up)"""
        if hand_landmarks is None:
            return False
        
        tips, pips = self.get_finger_landmarks(hand_landmarks)
        index_up = self.is_index_finger_up(tips, pips)
        
        # Detect rising edge (finger just went up)
        gesture_detected = index_up and not self.prev_index_up
        self.prev_index_up = index_up
        
        if gesture_detected:
            self.jump_count += 1
            print(f"🚀 JUMP #{self.jump_count} DETECTED!")
        
        return gesture_detected

    def draw_landmarks_and_status(self, image, results, gesture_detected: bool):
        """Draw hand landmarks and gesture status on the image"""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                self.mp_drawing.draw_landmarks(
                    image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Highlight index finger
                index_tip = hand_landmarks.landmark[8]
                h, w, _ = image.shape
                cx, cy = int(index_tip.x * w), int(index_tip.y * h)
                
                # Draw circle on index finger tip
                color = (0, 255, 0) if self.prev_index_up else (0, 0, 255)
                cv2.circle(image, (cx, cy), 15, color, -1)
                
                # Add finger label
                cv2.putText(image, "INDEX", (cx-30, cy-20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # Draw status text
        status_text = "Index Finger UP - READY TO JUMP!" if self.prev_index_up else "Index Finger DOWN - Fist Position"
        status_color = (0, 255, 0) if self.prev_index_up else (0, 0, 255)
        
        # Background rectangle for better text visibility
        cv2.rectangle(image, (5, 5), (635, 90), (0, 0, 0), -1)
        cv2.rectangle(image, (5, 5), (635, 90), (255, 255, 255), 2)
        
        cv2.putText(image, status_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
        
        if gesture_detected:
            cv2.putText(image, f"🚀 JUMP #{self.jump_count} DETECTED!", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        # Jump counter
        cv2.putText(image, f"Total Jumps: {self.jump_count}", (10, image.shape[0] - 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Instructions
        cv2.putText(image, "Press 'q' to quit", (10, image.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    def run(self):
        """Main loop for gesture detection demo"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert BGR to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process frame
            results = self.hands.process(rgb_frame)
            
            # Detect gesture
            gesture_detected = False
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    gesture_detected = self.detect_jump_gesture(hand_landmarks)
                    if gesture_detected:
                        break
            else:
                # No hand detected, reset state
                self.prev_index_up = False
            
            # Draw landmarks and status
            self.draw_landmarks_and_status(frame, results, gesture_detected)
            
            # Display frame
            cv2.imshow('Gesture Detection Demo', frame)
            
            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()
        
        print(f"\n🎉 Demo complete! Total jumps detected: {self.jump_count}")

if __name__ == "__main__":
    demo = GestureDemo()
    demo.run() 