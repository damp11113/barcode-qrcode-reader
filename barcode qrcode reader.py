import cv2
from pyzbar import pyzbar
from gtts import gTTS
from playsound import playsound
import os
from time import sleep

a = 0


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')

        # 3
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
            playsound('Barcodefx.mp3')
            print(barcode_info)
            tts = gTTS(text=barcode_info, lang='th')
            tts.save('barcode.mp3')
            playsound('barcode.mp3')
            os.remove('barcode.mp3')
            ff = a + 1

    return frame


def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()