from tkinter import *
from tkinter import filedialog
import AddStudent
import convertImageIntoPkl as convert
import makingSpreadSheet as mkss
import faceDetect as fd 
import drawBox

def main_screen():
    global screen1
    screen1=Tk()
    screen1.geometry('500x500')
    screen1.title('Face Recognition Based Attendance System')
    
    label_a=Label(screen1,text=" ")
    label_a.grid(row=0,column=0)
    
    label_text=Label(screen1,text="FR Based Attendance System",fg="white",bg="black")
    label_text.grid(row=1,column=2)
    
    label_a=Label(screen1,text=" ")
    label_a.grid(row=2,column=0)
    
    button1=Button(screen1,text="Add Student",bg='light blue',relief='raised',height='6',width=20,command=add_student)
    button1.grid(row=3,column=1)
    
    button2=Button(screen1,text="Convert Images To PKL",bg='light blue',relief='raised',height='6',width=20,command=images_to_pkl)
    button2.grid(row=3,column=3)
    
    label_a=Label(screen1,text=" ")
    label_a.grid(row=4,column=0)
    
    button3=Button(screen1,text="Making Spreadsheet",bg='light blue',relief='raised',height='6',width=20,command=make_spreadsheet)
    button3.grid(row=5,column=1)
    
    button4=Button(screen1,text="Detect Face",bg='light blue',relief='raised',height='6',width=20,command=detect_face)
    button4.grid(row=5,column=3)
    
    label_a=Label(screen1,text=" ")
    label_a.grid(row=6)
    
    button5=Button(screen1,text="Detect By Photo",bg='light blue',relief='raised',height='6',width=20,command=detect_by_photo)
    button5.grid(row=7,column=1)
    
    
    screen1.mainloop()
    
def add_student():
    #screen2=Toplevel(screen1)
    global screen2,frame1,frame2
    
    
    
    screen2=Tk()
    
    frame1=Frame(screen2)
    frame1.pack()
    
    frame2=Frame(screen2)
    frame2.pack()
    
    screen2.title('Add Student')
    screen2.geometry('300x300')
    
    
    global studentname,studentregd,ename,eregd
    
    studentname=StringVar()
    studentregd=StringVar()
    
    label1=Label(frame1,text="Add Student",bg='grey',height='2',width='300')
    label1.pack()
    
    label_a=Label(frame1,text=" ")
    label_a.pack()
    
    labelname=Label(frame1,text='Name',font=('Calibri',13))
    labelname.pack()
    
    
    
    ename=Entry(frame1,textvariable=studentname)
    ename.pack()
    
    label_a=Label(frame1,text=" ")
    label_a.pack()
    
    labelregd=Label(frame1,text='RegdNo.',font=('Calibri',13))
    labelregd.pack()
    
    eregd=Entry(frame1,textvariable=studentregd)
    eregd.pack()
    
    
    
    buttonSubmit=Button(frame1,text="Submit",bg='light green',width='10',command=submitStudent)
    
    buttonSubmit.pack()
    
    buttonReset=Button(frame1,text="Reset",bg='light green',width='10',command=resetStudent)
    
    buttonReset.pack()
    
    global labelSuccess
    labelSuccess=Label(frame2,text='Successfuly Registered!!!!')
    
    #print(studentname.get(),studentregd.get())
    
    #label1.pack()
    screen2.mainloop()
    
    
def submitStudent():
    
    label_a=Label(frame1,text=" ")
    label_a.pack()
    
    
    #print('student name=',ename.get())
    AddStudent.add_student(ename.get(),eregd.get())
    
    
    labelSuccess.grid(row=0,column=3)
    
def resetStudent():
    
    ename.delete(0,END)
    eregd.delete(0,END)
    
    labelSuccess.grid_forget()
    
    
    
def images_to_pkl():
    
    screen3=Tk()
    screen3.title('Convert Images To PKL')
    screen3.geometry('300x300')
    
    label_a=Label(screen3,text=" ")
    label_a.pack()
    
    label_a=Label(screen3,text=" ")
    label_a.pack()
    
    buttonAll=Button(screen3,text='All Students',width=10,command=images_to_pkl_all)
    buttonAll.pack()
    
    label_a=Label(screen3,text=" ")
    label_a.pack()
    
    labelregd=Label(screen3,text='RegdNo.',font=('Calibri',13))
    labelregd.pack()
    
    global eregdImageToPkl
    
    studentregd=StringVar()
    eregdImageToPkl=Entry(screen3,textvariable=studentregd)
    eregdImageToPkl.pack()
    
    buttonSubmit=Button(screen3,text="Submit",bg='light green',width='10',command=images_to_pkl_one)
    buttonSubmit.pack()
    
    screen3.mainloop()
    
    
def images_to_pkl_all():
    convert.allStudents()
    
def images_to_pkl_one():
    convert.oneStudent(eregdImageToPkl.get())
    
def make_spreadsheet():
    mkss.making_spread_sheet()

def detect_face():
    fd.face_detect()
    
    
def detect_by_photo():
    
    screen4=Tk()
    screen4.geometry('200x200')
    screen4.title('Detect By Photo')
    label_a=Label(screen4,text=" ")
    label_a.grid(row=0)
    
    
    label_a=Label(screen4,text=" ")
    label_a.grid(row=1)
    
    global ebrowse
    ebrowse=Entry(screen4)
    ebrowse.grid(row=2,column=1,columnspan=9)
    
    button1=Button(screen4,text='Browse',command=browse)
    button1.grid(row=2,column=11)
    
    button2=Button(screen4,text='Detect Photo',command=detect_button)
    button2.grid(row=3,column=3)
    screen4.mainloop()
    
def browse():
    global filename
    filename=filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg;*.jpeg"),("png files","*.png")))
    
    ebrowse.insert(END,filename)
    print(filename)
    
def detect_button():
    drawBox.detect_by_photo(filename)


main_screen()