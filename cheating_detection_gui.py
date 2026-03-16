import cv2
import mediapipe as mp
import face_recognition
import threading
import time
import os
import pandas as pd
from datetime import datetime
from playsound import playsound
import smtplib
from email.message import EmailMessage

# Config
AUTHORIZED_IMAGE = "authorized_user.jpg"
LOG_FILE = "cheating_log.csv"
ALERT_SOUND = "alert.mp3"
SCREENSHOT_DIR = "violations"
EMAIL_RECEIVER = "sanjay036k@gmail.com"  # Change to real email
EMAIL_SENDER = "anshu25082005@gmail.com"
EMAIL_PASSWORD = "gsljiipioqvrlxsd"

# Create folder
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Setup
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(max_num_faces=2, refine_landmarks=True)
mp_draw = mp.solutions.drawing_utils

# Known face encoding
known_face = face_recognition.load_image_file(AUTHORIZED_IMAGE)
known_encoding = face_recognition.face_encodings(known_face)[0]

def play_alert():
    threading.Thread(target=playsound, args=(ALERT_SOUND,), daemon=True).start()

def send_email(status, image_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = f'ALERT: {status}'
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg.set_content(f'Violation detected: {status}\nTime: {datetime.now()}')

        with open(image_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='png', filename=os.path.basename(image_path))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"[EMAIL SENT] {status}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")

def is_verified_user(frame):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    encodings = face_recognition.face_encodings(small_frame)
    for encoding in encodings:
        matches = face_recognition.compare_faces([known_encoding], encoding)
        if True in matches:
            return True
    return False

def is_looking_away(landmarks):
    nose = landmarks[1]
    return nose.x < 0.3 or nose.x > 0.7

def is_eyes_closed(landmarks):
    left_y = abs(landmarks[385].y - landmarks[380].y)
    right_y = abs(landmarks[160].y - landmarks[144].y)
    return (left_y + right_y) / 2 < 0.01

def log_violation(status, frame):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"{SCREENSHOT_DIR}/{status.replace(' ', '_')}_{timestamp}.png"
    cv2.imwrite(path, frame)
    send_email(status, path)

    # Log to CSV
    log_row = {'Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Status': status}
    df = pd.DataFrame([log_row])
    if not os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)

# Start webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)
    status = "Normal"

    if result.multi_face_landmarks:
        if len(result.multi_face_landmarks) > 1:
            status = "Multiple faces detected"
        else:
            for face_landmarks in result.multi_face_landmarks:
                mp_draw.draw_landmarks(frame, face_landmarks, mp_face.FACEMESH_TESSELATION)
                if is_looking_away(face_landmarks.landmark):
                    status = "Looking away"
                elif is_eyes_closed(face_landmarks.landmark):
                    status = "Eyes closed"
                elif not is_verified_user(frame):
                    status = "Unverified user detected"
    else:
        status = "No face detected"

    # Display
    color = (0, 255, 0) if status == "Normal" else (0, 0, 255)
    cv2.putText(frame, f"Status: {status}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Cheating Detection", frame)

    # Trigger actions
    if status != "Normal":
        play_alert()
        log_violation(status, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
