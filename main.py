import cv2
import pytesseract as pt
import pyttsx3
import pyautogui
from spellchecker import SpellChecker

spell = SpellChecker(language='pt') #Dicionário português - Portugal
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#pt.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe")
pt.pytesseract.tesseract_cmd = (r"C:/Users/adrie\Desktop/camera/Tesseract-OCR/Tesseract.exe")


config = r'--oem 2 --psm 6 '            # OK:  r'--oem 2 --psm 6'

video = cv2.VideoCapture()
ip = "https://192.168.43.181:8080/video"    #SEPTO:"https://10.0.0.100:8080/video"         #"https://192.168.0.100:8080/video" 
video.open(ip)



while True:
    check, img = video.read()
    img = cv2.resize(img, (640, 480))    
    img = cv2.transpose(img)
    img = cv2.flip(img, 1)
    cv2.imshow("img", img)
    cv2.imwrite("capture.png", img)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break

imagem = cv2.imread("capture.png")
frase = pt.pytesseract.image_to_string(imagem, lang= "por", config = config)




#words: list = frase.split()
#list_of_correct_words = [spell.correction(word) for word in words if spell.correction(word) is not None]
#string_sem_loop = ' '.join(list_of_correct_words)
#print (string_sem_loop)






print(frase)
engine.say(frase)
engine.runAndWait()







#caixas = (pt.pytesseract.image_to_boxes(imagem))
#imH,imW,_ = imagem.shape

#for b in caixas.splitlines():
    #b = b.split(' ')
    #letra,x,y,w,h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])   
    #cv2.rectangle(imagem,(x,imH-y),(w,imH-h),(0,0,255),1)

#cv2.imshow("resultado",imagem)
#cv2.waitKey(0)
