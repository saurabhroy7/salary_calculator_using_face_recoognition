import tkinter as tk
from tkinter import Label
import cv2
import os
import face_recognition
from datetime import datetime
from datetime import date
import numpy
import subprocess


cA, cM, cSh, cV, cH, cT, cSa = 0, 0, 0, 0, 0, 0, 0
gA, gM, gSh, gV, gH, gT, gSa = 0, 0, 0, 0, 0, 0, 0

salary =0
matchStatus ={}
def mark_att_stu():
    global gA, gM, gSh, gV, gH, gT, gSa ,cA, cM, cSh, cV, cH, cT, cSa, salary, matchStatus
    path = 'tasveer'
    images = []
    classNames = []

    # to print the names of jpg file
    myList = os.listdir(path)
    print(myList)

    for cls in myList:
        curImg = cv2.imread(f'{path}/{cls}')

        # for splitting the .jpg extension

        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    # function for finding encoding of images

    def finding_encodings(images):
        encodeList = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)

        return encodeList

    knownEncodings = finding_encodings(images)
    # print(len(knownEncodings))
    print("Encoding Complete")

    # writing attendance in csv file

    def markattendance(name):

        with open('sal.csv', 'r+') as f:
            mydataList = f.readlines()
            nameList = []



            for line in mydataList:
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                curDate = date.today()
                forDate = curDate.strftime('%B %d')
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{forDate},{dtString}')

    # captures webcam id is 0

    cap = cv2.VideoCapture(0)

    while True:

        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurrFrame = face_recognition.face_locations(imgS)
        encodeCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)
        text = 'Press ESC to Exit'
        cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
        for encodeFace, faceLoc in zip(encodeCurrFrame, facesCurrFrame):

            matches = face_recognition.compare_faces(knownEncodings, encodeFace)
            faceDis = face_recognition.face_distance(knownEncodings, encodeFace)

            # print(faceDis)

            matchIndex = numpy.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                if matchStatus.get(name) is None:
                    matchStatus[name] = True
                    if name == "SAURABH":
                        cSa+=1
                    elif name == "ANKIT":
                        cA+=1
                    elif name =="MANISHA":
                        cM+=1
                    elif name =="KARTAVYA":
                        cSh+=1
                    elif name =="VANSHIKA":
                        cV+=1
                    elif name =="HANI":
                        cH+=1
                    elif name =="TARUN":
                        cT+=1





                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markattendance(name)


        cv2.imshow('Webcam', img)

        # For returning to main menu

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cap.release()
            cv2.destroyWindow('Webcam')
            return

def total_salary():
    def button_ankit():
        gA= cA*800
        window = tk.Tk()
        window.title("Ankit")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gA} ")
        label.pack()
        window.mainloop()


    def button_hani():
        gH = cH * 800
        window = tk.Tk()
        window.title("Hani")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gH} ")
        label.pack()
        window.mainloop()


    def button_mani():
        gM = cM * 800
        window = tk.Tk()
        window.title("Manisha")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gM} ")
        label.pack()
        window.mainloop()


    def button_vanshi():
        gV = cV * 800
        window = tk.Tk()
        window.title("Vanshika")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gV} ")
        label.pack()
        window.mainloop()


    def button_sharad():
        gSh = cSh * 800
        window = tk.Tk()
        window.title("Sharad")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gSh} ")
        label.pack()
        window.mainloop()


    def button_sau():
        gSa = cSa * 800
        window = tk.Tk()
        window.title("Saurabh")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gSa} ")
        label.pack()
        window.mainloop()


    def button_tarun():
        gA = cA * 800
        window = tk.Tk()
        window.title("Tarun")
        window_width = 300
        window_height = 50
        window.geometry(f"{window_width}x{window_height}")
        label = Label(window, text=f"Salary is {gA} ")
        label.pack()
        window.mainloop()

    # window for view salary

    window = tk.Tk()
    window.title("Salary")
    window_width = 300
    window_height = 400
    window.geometry(f"{window_width}x{window_height}")

    # Create a frame to hold the buttons
    frame = tk.Frame(window)

    # Create Button A for ankit
    buttonA = tk.Button(frame, text="Ankit", command=button_ankit)
    buttonA.pack(pady=10)

    # Create Button B for hani
    buttonB = tk.Button(frame, text="Hani", command=button_hani)
    buttonB.pack(pady=10)

    # Create Button C for manisha
    buttonC = tk.Button(frame, text="Manisha", command=button_mani)
    buttonC.pack(pady=10)

    # Create Button D for vanshika
    buttonD = tk.Button(frame, text="Vanshika", command=button_vanshi)
    buttonD.pack(pady=10)

    #Create Button E for Sharad
    buttonE = tk.Button(frame, text="Sharad", command=button_sharad)
    buttonE.pack(pady=10)

    #Create Button F for Saurabh
    buttonF = tk.Button(frame, text="Saurabh", command=button_sau)
    buttonF.pack(pady=10)

    #Create button G for Tarun
    buttonG = tk.Button(frame, text="Tarun", command=button_tarun)
    buttonG.pack(pady=10)

    # Pack the frame within the window
    frame.pack(expand=True)

    # Calculate the coordinates to center the window
    x = (window.winfo_screenwidth() - window_width) // 2
    y = (window.winfo_screenheight() - window_height) // 2

    # Set the window position
    window.geometry(f"+{x}+{y}")

    # Run the main window loop
    window.mainloop()

def open_csv():
    # Specify the path to your CSV file
    csv_file_path = "sal.csv"

    # Use the subprocess module to open the CSV file with the default application
    subprocess.run(['start', csv_file_path], shell=True)
# Functions to be called when buttons are clicked


def button1_click():
    mark_att_stu()

def button2_click():
    total_salary()

def button3_click():
    open_csv()

def button4_click():
    cv2.destroyAllWindows()
    quit()


# Create the main window
window = tk.Tk()

window.title("Main Menu")
# Set the window dimensions
window_width = 400
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Create a frame to hold the buttons
frame = tk.Frame(window)

# Create Button 1
button1 = tk.Button(frame, text="Mark Attendance", command=button1_click)
button1.pack(pady=10)

# Create Button 2
button2 = tk.Button(frame, text="View Salary", command=button2_click)
button2.pack(pady=10)

# Create Button 3
button3 = tk.Button(frame, text="View Detailed Record", command=button3_click)
button3.pack(pady=10)

# Create Button 3
button4 = tk.Button(frame, text="Exit", command=button4_click)
button4.pack(pady=10)

# Pack the frame within the window
frame.pack(expand=True)

# Calculate the coordinates to center the window
x = (window.winfo_screenwidth() - window_width) // 2
y = (window.winfo_screenheight() - window_height) // 2

# Set the window position
window.geometry(f"+{x}+{y}")

# Run the main window loop
window.mainloop()