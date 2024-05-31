#Importing OpenCV Library for basic image processing functions
import cv2
# Numpy for array related functions
import numpy as np
# Dlib for deep learning based Modules and face landmark detection
import dlib
#face_utils for basic operations of conversion
from imutils import face_utils
import urllib.request

import time
import json
import requests

# Function to update JSON file with current states
def update_json_file(filename, states):
    with open(filename, 'w') as file:
        json.dump(states, file)

# Function to read JSON file
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to send data to ESP8266
def send_data_to_esp(data):
    url = 'http://192.168.43.174/test'  # Replace ESP8266_IP_ADDRESS with the IP address of your ESP8266
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Data sent successfully to ESP8266")
    else:
        print("Failed to send data to ESP8266")


#Initializing the camera and taking the instance
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#status marking for current state
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)

def compute(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist

def blinked(a,b,c,d,e,f):
	up = compute(b,d) + compute(c,e)
	down = compute(a,f)
	ratio = up/(2.0*down)

	#Checking if it is blinked
	if(ratio>0.25):
		return 2
	elif(ratio>0.21 and ratio<=0.25):
		return 1
	else:
		return 0


while True:
    imgResp=urllib.request.urlopen('http://192.168.43.148/capture')
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    # _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    #detected face in faces array
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        #The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36],landmarks[37], 
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42],landmarks[43], 
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        #Now judge what to do for the eye blinks
        if(left_blink == 0 or right_blink == 0):
            sleep += 1
            drowsy = 0
            active = 0
            if(sleep > 6):
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                filename = 'result.json'  # Replace with the path to your JSON file
                states = {'state': 'sleeping'}  # Example state, replace with actual logic
                update_json_file(filename, states)
                image_processing_states = read_json_file(filename)
                send_data_to_esp(image_processing_states)

        elif(left_blink == 1 or right_blink == 1):
            sleep = 0
            active = 0
            drowsy += 1
            if(drowsy > 6):
                status = "Drowsy !"
                color = (0, 0, 255)
                filename = 'result.json'  # Replace with the path to your JSON file
                states = {'state': 'drowsy'}  # Example state, replace with actual logic
                update_json_file(filename, states)
                image_processing_states = read_json_file(filename)
                send_data_to_esp(image_processing_states)

        else:
            drowsy = 0
            sleep = 0
            active += 1
            if(active > 6):
                status = "Active :)"
                color = (0, 255, 0)
                filename = 'result.json'  # Replace with the path to your JSON file
                states = {'state': 'active'}  # Example state, replace with actual logic
                update_json_file(filename, states)
                image_processing_states = read_json_file(filename)
                send_data_to_esp(image_processing_states)

        	
        cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)


    cv2.imshow("Frame", frame)
    # cv2.imshow("Result of detector", frame)
    key = cv2.waitKey(1)
    if key == 27:
      	break