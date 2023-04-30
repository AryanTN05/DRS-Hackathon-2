import streamlit as st
import cv2
from model import FacialExpressionModel
import numpy as np

facec = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#model = FacialExpressionModel("model_v1.json", "model_weights_v1.h5")
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

def main():
    cap = cv2.VideoCapture(0)
    video_placeholder = st.empty()
    result_placeholder = st.empty()

    # returns camera frames along with bounding boxes and predictions
    while True:
        _, fr = cap.read()

        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
        
        video_frame = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)
        video_placeholder.image(video_frame, channels="RGB")

        result_placeholder.text(pred)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

    return

if __name__ == "__main__":
    main()