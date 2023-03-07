import cv2
import pytesseract as pt
import pyttsx3
import pyautogui
from spellchecker import SpellChecker

spell = SpellChecker(language='pt') #Dicionário português - Portugal
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate', 150)
pt.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe")
config = r'--oem 2 --psm 6'            # OK:  r'--oem 2 --psm 6'

video = cv2.VideoCapture()
ip = "https://192.0.0.4:8080/video"    #SEPTO:"https://10.0.0.100:8080/video"         #"https://192.168.0.100:8080/video" 
video.open(ip)

#USAR DEPOIS:
#imagem_ajustada = cv2.threshold(imagem_ajustada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #dá um contraste ao branco e preto
#imagem_ajustada = cv2.Canny(imagem_ajustada, 100, 200) #dar uma olha

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
words: list = frase.split()
list_of_correct_words = [spell.correction(word) for word in words if spell.correction(word) is not None]
string_sem_loop = ' '.join(list_of_correct_words)
print (string_sem_loop)
engine.say(string_sem_loop)
engine.runAndWait()




