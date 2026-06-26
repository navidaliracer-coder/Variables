#In this activity, students will build a real-time gesture-controlled photo app that allows them to apply different filters (grayscale, sepia, negative, blur) and take screenshots using hand gestures.

import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands
TIP =  H.HandLandmark
ids = {
    "Thumb": TIP.THUMB_TIP,
    "Index": TIP.INDEX_FINGER_TIP,
    "Middle": TIP.TIP.MIDDLE_FINGER_TIP,
    "RING": TIP.RING_FINGER_TIP
    "pinky": 

}