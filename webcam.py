import cv2
import pytesseract as pt
import pyttsx3

engine = pyttsx3.init()
pt.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe")

video = cv2.VideoCapture(0)

while True:
    check, img = video.read()
    img = cv2.resize(img, (640, 480))    
    cv2.imshow("img",img)
    cv2.imwrite("capture.png", img)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break



imagem = cv2.imread("capture.png")
print(pt.pytesseract.image_to_string(imagem, lang= "por"))
caixas = (pt.pytesseract.image_to_boxes(imagem))
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("resultado", gray)
imH,imW,_ = imagem.shape

for b in caixas.splitlines():
    b = b.split(' ')
    letra,x,y,w,h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(imagem,(x,imH-y),(w,imH-h),(0,0,255),1)




cv2.imshow("resultado",imagem)
cv2.waitKey(0)
