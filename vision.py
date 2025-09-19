import cv2
import numpy as np

def preprocess_image(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, binary = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def find_hand_contour(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(contours, key=cv2.contourArea) if contours else None

def count_fingers_from_contour(contour, canvas):
    hull = cv2.convexHull(contour, returnPoints=False)
    if hull is None or len(hull) < 3:
        return 0

    defects = cv2.convexityDefects(contour, hull)
    if defects is None:
        return 0

    count = 0
    for i in range(defects.shape[0]):
        s, e, f, _ = defects[i, 0]
        start, end, far = contour[s][0], contour[e][0], contour[f][0]
        a = np.linalg.norm(end - start)
        b = np.linalg.norm(far - start)
        c = np.linalg.norm(end - far)
        angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c + 1e-5))
        if angle < np.pi / 2:
            count += 1
            cv2.circle(canvas, tuple(far), 6, (255, 0, 0), -1)
    return count

def classify_sign(finger_count):
    mapping = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G"
    }
    return mapping.get(finger_count, "UNKNOWN")