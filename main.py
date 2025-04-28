from openai_interview.interview_manager import InterviewManager
from facial_recognition.emotion_detector import EmotionDetector
import cv2

def main():
    topic = input("Enter interview topic: ")
    nao_ip = input("Enter NAO robot IP address: ")

    interview = InterviewManager(topic, nao_ip)
    emotion_detector = EmotionDetector()

    cap = cv2.VideoCapture(0)

    try:
        while True:
            interview.conduct_interview()

            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            emotion = emotion_detector.detect_emotion(frame)
            print(f"Detected emotion: {emotion}")

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        interview.close()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
