# AI-Based Online Exam Proctoring System

## 📌 Project Overview

The **AI-Based Online Exam Proctoring System** is an intelligent monitoring system designed to detect and prevent cheating during online examinations.

The system uses **Computer Vision and Artificial Intelligence techniques** to analyze student behavior in real time using the webcam. It detects suspicious activities such as **looking away from the screen, multiple faces, absence of the candidate, and unusual movements**.

The project is implemented using **Python, OpenCV, MediaPipe, and Face Recognition libraries**, and includes **logging, audio alerts, and a monitoring dashboard** for administrators.

---

# 🎯 Objectives

* Monitor students during online exams using AI.
* Detect suspicious behavior automatically.
* Log violations with timestamps.
* Provide real-time alerts.
* Maintain exam integrity through automated proctoring.

---

# 🛠 Technology Stack

## Programming Language

* **Python**

## Computer Vision Libraries

* **OpenCV** – Video capture and image processing
* **MediaPipe** – Face mesh, head pose, and eye tracking
* **Face Recognition** – Candidate identity verification

## Data Processing

* **Pandas** – Log management and analysis

## Additional Tools

* **SMTP (Email Module)** – Send violation alerts to admin
* **PlaySound** – Audio warning alerts
* **Threading** – Parallel monitoring processes

---

# 📷 System Features

## 1️⃣ Face Detection

The system continuously detects faces using the webcam.

Capabilities:

* Detect if **no face is present**
* Detect **multiple faces**
* Trigger alerts for suspicious situations

---

## 2️⃣ Face Recognition

The system verifies the identity of the candidate.

Process:

* Compare live webcam feed with stored candidate image
* Confirm identity before exam begins

---

## 3️⃣ Head Pose and Eye Tracking

Using **MediaPipe Face Mesh**, the system tracks:

* Head orientation
* Eye direction
* Face landmarks

This helps detect behaviors such as:

* Looking away from the screen
* Excessive head movement
* Possible cheating attempts

---

## 4️⃣ Real-Time Alerts

If suspicious activity is detected:

* An **audio warning** is played
* A **violation entry is logged**
* The admin can be notified

---

## 5️⃣ Violation Logging

All detected violations are recorded in a log file.

Each log entry contains:

* Timestamp
* Type of violation
* Candidate information

Logs are stored in **CSV format** using Pandas.

Example log entry:

```id="f2a6r8"
Timestamp,Violation
2025-03-10 10:05:12,Multiple Faces Detected
```

---

## 6️⃣ Admin Notification

The system can send **email alerts** to the exam administrator.

Using SMTP, the system sends:

* Candidate details
* Violation information
* Timestamp

This ensures **immediate monitoring of exam integrity**.

---

# ⚙️ Working of the System

1️⃣ The webcam starts capturing video using **OpenCV**.

2️⃣ **Face detection and recognition** verify the candidate's identity.

3️⃣ **MediaPipe Face Mesh** tracks facial landmarks.

4️⃣ The system detects suspicious behaviors such as:

* Looking away from the screen
* Multiple faces appearing
* Candidate leaving the frame

5️⃣ When a violation occurs:

* An **audio alert** is triggered.
* A **log entry** is created.
* An **email notification** may be sent.

---

# 📂 Project Structure

```id="hks9aj"
online-exam-proctoring/
│
├── proctoring.py
├── face_database/
│   └── student.jpg
│
├── logs/
│   └── violations.csv
│
├── dashboard/
│   └── dashboard.py
│
├── alert_sound.mp3
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash id="n8dpx5"
git clone https://github.com/AnshuKumar25/online-exam-proctoring.git
```

---

## 2️⃣ Install Dependencies

```bash id="v5qz7r"
pip install opencv-python
pip install mediapipe
pip install face-recognition
pip install pandas
pip install playsound
```

Or install using requirements file:

```bash id="c6yxm3"
pip install -r requirements.txt
```

---

## 3️⃣ Run the Proctoring System

```bash id="u2vld9"
python proctoring.py
```

The webcam will start monitoring the candidate.

---

# 📊 Example Violations Detected

* No face detected
* Multiple faces detected
* Looking away from screen
* Unauthorized movement

Each violation is logged and optionally notified to the administrator.

---

# 📚 Concepts Demonstrated

* Computer Vision
* Face Recognition
* Real-time Video Processing
* AI-based Behavior Monitoring
* Event Logging and Alerts
* Automated Proctoring Systems

---

# 🔮 Future Enhancements

* Web-based admin dashboard
* AI-based cheating classification
* Screen monitoring
* Multi-camera support
* Cloud-based exam monitoring
* Automatic exam termination on repeated violations

---

# 👨‍💻 Author

**Anshu Kumar**

Computer Science & Engineering Student

---

# 📜 License

This project is developed for **educational and research purposes related to AI-based exam monitoring systems**.
