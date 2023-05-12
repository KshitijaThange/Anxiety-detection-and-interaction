import cv2
import numpy as np
from keras.models import model_from_json

anxiety_dict = {0:"High_Anx", 1:"Low_Anx", 2:"No_Anx"}

#load Json
json_file = open('anxiety_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
anxiety_model = model_from_json(loaded_model_json)

# load weights into new model
anxiety_model.load_weights("anxiety_model.h5")
print("loaded model from disk")


# start the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 500))
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 4)
        roi_gray = gray_frame[y:y+h, x:x+w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray,(48, 48)), -1), 0)

        #predict the anxiety
        anxiety_prediction = anxiety_model.predict(cropped_img)
        maxindex = int(np.argmax(anxiety_prediction))
        cv2.putText(frame, anxiety_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_4)


    cv2.imshow('ANXIETY', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()