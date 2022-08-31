import  RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
#Se dice que se esta listo para leer la tarjeta
print("Place Tag")

try:
   #Se imprime el id  al usuario  de  la tarjeta
         id.text = reader.read()
         print (id)
         print (text)
finally:
       GPIO.cleanup()


