import pickle
import os
from stat import *
import face_recognition


def oneStudent(regdNo):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolderPath=os.path.join(currentDir,'Images\\'+str(regdNo))
    pklFolderPath=os.path.join(currentDir,'Pkl\\'+str(regdNo))

    for images in os.listdir(imageFolderPath):
        image=face_recognition.load_image_file(imageFolderPath+"\\"+images)
        face_encoding=face_recognition.face_encodings(image)[0]
        filename=images[:-4]
        with open(pklFolderPath+'\\'+filename+'.pkl','wb') as pickle_file:
            pickle.dump(face_encoding,pickle_file)


def allStudents():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolderPath=os.path.join(currentDir,'Images')
    pklFolderPath=os.path.join(currentDir,'Pkl')

    for files in os.listdir(imageFolderPath):
        pathname=os.path.join(imageFolderPath,files)
        mode=os.stat(pathname)[ST_MODE]

        if S_ISDIR(mode):
            for images in os.listdir(pathname):
                image=face_recognition.load_image_file(pathname+"\\"+images)
                face_encoding=face_recognition.face_encodings(image)[0]
                filename=images[:-4]
                with open(pklFolderPath+'\\'+files+'\\'+filename+'.pkl','wb') as pickle_file:
                    pickle.dump(face_encoding,pickle_file)