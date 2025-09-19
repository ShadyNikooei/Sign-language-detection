import cv2
import pyttsx3
from vision import preprocess_image, find_hand_contour, count_fingers_from_contour, classify_sign
from actions import load_actions, perform_action
from logger import log_action

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
last_sign = None
actions_map = load_actions()
detected_sequence = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    roi = frame[100:400, 100:400]
    binary = preprocess_image(roi)
    contour = find_hand_contour(binary)
    canvas = roi.copy()
    sign = "No Hand"

    if contour is not None:
        cv2.drawContours(canvas, [contour], -1, (0, 255, 0), 2)
        fingers = count_fingers_from_contour(contour, canvas)
        sign = classify_sign(fingers)

        if sign != last_sign and sign != "UNKNOWN":
            print(f"Detected sign: {sign}")
            detected_sequence += sign
            perform_action(sign, actions_map)
            engine.say(f"Sign {sign} detected")
            engine.runAndWait()
            log_action(sign)
            last_sign = sign

        if len(detected_sequence) > 3:
            detected_sequence = detected_sequence[-3:]
        if detected_sequence in actions_map:
            print(f"Macro matched: {detected_sequence}")
            perform_action(detected_sequence, actions_map)
            log_action(detected_sequence)
            detected_sequence = ""

    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 255), 2)
    cv2.putText(frame, f"Sign: {sign}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.putText(frame, f"Sequence: {detected_sequence}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Sign Detection", frame)
    cv2.imshow("Binary", binary)
    cv2.imshow("ROI", canvas)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()