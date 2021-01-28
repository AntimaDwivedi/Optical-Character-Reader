import cv2
import time
import imutils
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cam = cv2.VideoCapture(0)
time.sleep(1)


def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text



while True:
    _, frame = cam.read()
    img=imutils.resize(frame,width=500)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera Feed", img)
    key = cv2.waitKey(10)& 0xFF
    if key == 27:
        cv2.imwrite("capture.png",img)
        info = recText('capture.png')
        print(info)
        file=open("result.txt","w")
        file.write(info)
        file.close()
        print("Written SuccessFul")
        break

cam.release()
cv2.destroyAllWindows()

