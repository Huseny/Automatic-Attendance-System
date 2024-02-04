import cv2
import numpy as np
from main import Recognizer


base_directory = '/home/husen/SE - 4 - 1/MAI/Attendance/attendance/attendance/recognition/models'

labels = np.load(f'{base_directory}/labels.npy')
label_dict = np.load(f'{base_directory}/label_dict.npy', allow_pickle=True).item()



recognizer = Recognizer(labels=labels, label_dict=label_dict)
recognizer.load_model(f'{base_directory}/fisherfaces.pkl')



def detect_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    return faces


def print_number_of_faces(detected_faces):
    num_faces = len(detected_faces)
    print(f"Number of faces detected: {detected_faces}")


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    detected_faces = detect_faces(frame)
    

    for x, y, w, h in detected_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        denoised_image = cv2.fastNlMeansDenoising(face, None, 10, 7, 21)
        flattened_image = denoised_image.flatten()

        label, label_idx, distance = recognizer.predict(flattened_image)

        print(f'Predicted label: {label}, distance: {distance}')
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


    print_number_of_faces(detected_faces)

    cv2.imshow('Face Detection', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

