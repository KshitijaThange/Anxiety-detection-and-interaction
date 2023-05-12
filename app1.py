from flask import Flask,render_template, Response
import cv2


app=Flask(__name__)
cap=cv2.VideoCapture(0)

def generate_frame():
      while True:
            ret,frame=cap.read()
            if not ret:
                  break
            else:
                  ret,buffer=cv2.imencode('.jpg',frame)
                  frame=buffer.tobytes()
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/anxiety_detect')
def anxiety_detect():
        return render_template('anxiety_detect.html')

@app.route('/webcam_anx')
def webcam_anx():
      return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
      app.run(debug=True)

