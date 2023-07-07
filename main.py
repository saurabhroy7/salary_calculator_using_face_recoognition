# import tkinter library for button
import tkinter as tk
from tkinter import Label

# import cv2 library to capture the images
import cv2

# import os library to give path
import os

# import face_recognition library to detect face
import face_recognition

# import datetime library to calculate current date and time
from datetime import datetime
from datetime import date

# import numpy to draw shape
import numpy

# import subprocess library
import subprocess

# To calculate the total number of days present in a month
cA, cM, cSh, cV, cH, cT, cSa = 0, 0, 0, 0, 0, 0, 0

# to calculate salary according to the total number of days
gA, gM, gSh, gV, gH, gT, gSa = 0, 0, 0, 0, 0, 0, 0

# initial salary value
salary =0
matchStatus ={}

# function to mark the attendance of the students by recognizing their faces
def mark_att_stu():

    # use global variables
    global gA, gM, gSh, gV, gH, gT, gSa,cA, cM, cSh, cV, cH, cT, cSa, salary, matchStatus

   """ path give the location of the images of the students which is stored in the attendanceimage folder  """
    path = 'attendanceimage'

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

    """ function for finding encoding of images by calcualting the distance between the the nose ,ear, eyes etc """
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

    """  writing the name of the student , which match in the attendanceimages in the csv file """
    def markattendance(name):

        # open csv file in read and write mode
        with open('data.csv', 'r+') as f:

            mydataList = f.readlines()
            nameList = []

            for line in mydataList:
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:

                """ calculates the current name and time with the help of the library current datetime """ 
                now = datetime.now()

                # store the current date in the curDate
                curDate = date.today()

                forDate = curDate.strftime('%B %d')
                dtString = now.strftime('%H:%M:%S')

               """  write the match name , current date and current time in the date time formatin the csv file """
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

                # convert match name in upper case
                name = classNames[matchIndex].upper()


                if matchStatus.get(name) is None:
                    matchStatus[name] = True

                    if name == "SAURABH":
                        cSa += 1

                    elif name == "ANKIT":
                        cA += 1

                    elif name == "MANISHA":

                        cM += 1

                    elif name == "SHARAD":
                        cSh += 1

                    elif name == "VANSHIKA":
                        cV += 1

                    elif name == "HANI":
                        cH += 1

                    elif name == "TARUN":
                        cT += 1


                y1, x2, y2, x1 = faceLoc

                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


                """ call the markattendance function to mark the attendance of the person by recognition their faces """
                markattendance(name)


        cv2.imshow('Webcam', img)

        # For returning to main menu
        k = cv2.waitKey(30) & 0xff

        if k == 27:

            """  to destroy or close the window of the camera after mark the attendance or match the face """
            cap.release()

            cv2.destroyWindow('Webcam')

            return



""" function to calculate the total salary using the total number of days present in a month """
def total_salary():

    def button_ankit()
        gA = cA*800

        window = tk.Tk()

        # window title
        window.title("Ankit")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gA} ")

        label.pack()

        window.mainloop()




def button_hani():

        gH = cH * 800
        window = tk.Tk()

        # window title
        window.title("Hani")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gH} ")

        label.pack()

        window.mainloop()

def button_mani():\

        gM = cM * 800

        window = tk.Tk()

        # window title
        window.title("Manisha")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gM} ")

        label.pack()

        window.mainloop()

    def button_vanshi():

        gV = cV * 800

        window = tk.Tk()

        # window title
        window.title("Vanshika")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gV} ")

        label.pack()

        window.mainloop()

def button_sharad():

        gSh = cSh * 800

        window = tk.Tk()

        # window title
        window.title("Sharad")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gSh} ")

        label.pack()

        window.mainloop()

    def button_sau():

        gSa = cSa * 800

        window = tk.Tk()

        # window title
        window.title("Saurabh")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gSa} ")

        label.pack()

        window.mainloop()

    def button_tarun():

        gA = cA * 800

        window = tk.Tk()

        # window title
        window.title("TARUN")

        # window width
        window_width = 200

        # window height
        window_height = 100

        # window area
        window.geometry(f"{window_width}x{window_height}")

        # print total salary
        label = Label(window, text=f"Salary is {gA} ")

        label.pack()

        window.mainloop()

    # window for view salary
    window = tk.Tk()

    # window title
    window.title("Salary")

    # window width
    window_width = 300

    # window height
    window_height = 400

    #window area
    window.geometry(f"{window_width}x{window_height}")

    # Create a frame to hold the buttons
    frame = tk.Frame(window)



    # Create Button A for ankit
    buttonA = tk.Button(frame, fg="red", bg="sky blue", text="      Ankit      ", command=button_ankit)

    # pack buttonA
    buttonA.pack(pady=10)
# Create Button B for hani
    buttonB = tk.Button(frame, fg="red", bg="sky blue", text="       Hani      ", command=button_hani)

    # pack buttonB
    buttonB.pack(pady=10)


    # Create Button C for manisha
    buttonC = tk.Button(frame, fg="red", bg="sky blue", text="  Manisha  ", command=button_mani)

    # pack buttonC
    buttonC.pack(pady=10)


    # Create Button D for vanshika
    buttonD = tk.Button(frame, fg="red", bg="sky blue", text="  Vanshika   ", command=button_vanshi)

    # pack buttonD
    buttonD.pack(pady=10)

    #Create Button E for Sharad
    buttonE = tk.Button(frame, fg="red", bg="sky blue", text="    Sharad    ", command=button_sharad)

    # pack buttonE
    buttonE.pack(pady=10)


    #Create Button F for Saurabh
    buttonF = tk.Button(frame, fg="red", bg="sky blue", text="    Saurabh   ", command=button_sau)

    # pack buttonF
buttonF.pack(pady=10)


    #Create button G for Tarun
    buttonG = tk.Button(frame, fg="red", bg="sky blue", text="      Tarun      ", command=button_tarun)

    # pack buttonG
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


""" function to open the csv file to see the record of the marked attendance of Person """ 
def open_csv():

    # Specify the path to your CSV file
    csv_file_path = "data.csv"

    # Use the subprocess module to open the CSV file with the default application
    subprocess.run(['start', csv_file_path], shell=True)


# Functions to be called when buttons are clicked

# create button1_click function to mark attendance

def button1_click():

    # call markattendance function
    mark_att_stu()


# create button2_click function to print total salary

def button2_click():

    """ call total salary function to calculate the salary according to the days present in a month """
    total_salary()


# create button3_click function to open csv file
def button3_click():

    # call open csv file
    open_csv()


# create button4_click function to destroy all windows
def button4_click():

    # destroy all windows
    cv2.destroyAllWindows()
    quit()

# Create the main window
window = tk.Tk()

# window title
window.title("Main Menu")

# Set the window width
window_width = 400

# Set the window width
window_height = 300

window.geometry(f"{window_width}x{window_height}")


# Create a frame to hold the buttons
frame = tk.Frame(window)


# Create Button 1
button1 = tk.Button(frame, bg="silver", fg="black", text="         Mark Attendance         ", command=button1_click)

# pack button1
button1.pack(pady=10)


# Create Button 2
button2 = tk.Button(frame,  bg="silver", fg="black", text="               View Salary             ", command=button2_click)

# pack button2
button2.pack(pady=10)


# Create Button 3
button3 = tk.Button(frame,  bg="silver", fg="black", text="      View Detailed Record      ", command=button3_click)

# pack button3
button3.pack(pady=10)


# Create Button 4
button4 = tk.Button(frame,  bg="silver", fg="black", text="                    Exit                     ", command=button4_click)

# pack button4
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

