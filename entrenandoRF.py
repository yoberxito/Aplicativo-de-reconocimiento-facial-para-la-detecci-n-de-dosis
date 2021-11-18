import cv2
import os
import numpy as np

dataPath = 'D:/ultimo ciclo/Integrador II/trabajo/data'
peoplelist = os.listdir(dataPath)
print('lista de personas ', peoplelist)
labels = []
facesData = []
label = 0
for nameDir in peoplelist:
    personPath = dataPath +'/' + nameDir
    print('leyendo las imagenes..')
    for fileName in os.listdir(personPath):
        print('Rostros ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitkey(10)
    label = label + 1
    #print('labels= ',labels)
    print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
    print('Numero de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))
    print('Numero de etiquetas 2: ',np.count_nonzero(np.array(labels)==2))
    print('Numero de etiquetas 3: ',np.count_nonzero(np.array(labels)==3))
    
    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    #Almacenando
    face_recognizer.write('modeloEigenFace.xml')
    print("Modelo almacenado")