# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import serial
import RPi.GPIO as GPIO
import adafruit_fingerprint

#usando puertos uart con sensor con hardware uart:
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

################################################## 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 16
GPIO.setup(PIR_PIN, GPIO.IN)

#################################################
def get_movement():
    """obtener la respuesta del sensor en una funcion"""
    print("esperando la lectura....")
    time.sleep(3)
    if GPIO.input(PIR_PIN):
        return True
    return False

##################################################

def get_fingerprint():
    """Obtener una imagen de la huella, modelarla,y ver si hay una igual!"""
    print("esperando por imagen...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Modelando...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    print("Buscando...")
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    return True


# pylint: disable=too-many-branches
def get_fingerprint_detail():
    """Obtener una imagen de la huella, modelarla, y ver si hay una igual!
    esta vez, se imprime error por una falla"""
    print("Obteniendo imagen...", end="", flush=True)
    i = finger.get_image()
    if i == adafruit_fingerprint.OK:
        print("Imagen tomada")
    else:
        if i == adafruit_fingerprint.NOFINGER:
            print("No hay dedo detectado")
        elif i == adafruit_fingerprint.IMAGEFAIL:
            print("Error de imagen")
        else:
            print("Otro error")
        return False

    print("Modelando...", end="", flush=True)
    i = finger.image_2_tz(1)
    if i == adafruit_fingerprint.OK:
        print("Modelado")
    else:
        if i == adafruit_fingerprint.IMAGEMESS:
            print("Imagen muy borrosa")
        elif i == adafruit_fingerprint.FEATUREFAIL:
            print("No se pudieron tomar caracteristicas")
        elif i == adafruit_fingerprint.INVALIDIMAGE:
            print("Imagen invalida")
        else:
            print("Otro error")
        return False

    print("Buscando...", end="", flush=True)
    i = finger.finger_fast_search()
    # pylint: disable=no-else-return
    # This block needs to be refactored when it can be tested.
    if i == adafruit_fingerprint.OK:
        print("Huella encontrada!")
        return True
    else:
        if i == adafruit_fingerprint.NOTFOUND:
            print("No hay otra igual")
        else:
            print("Otro error")
        return False


##################################################


def get_num(max_number):
    """se usa para tener una libreria cone l tamaÃ±o maximo de huellas por guardar"""
    i = -1
    while (i > max_number - 1) or (i < 0):
        try:
            i = int(input("Ingrese un  ID # from 0-{}: ".format(max_number - 1)))
        except ValueError:
            pass
    return i
#########################################################
print('La lectura empezara en 5 segundos')
time.sleep(5)
print ('listo')


while True:
    print("-------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates: ", finger.templates)
    if finger.count_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Number of templates found: ", finger.template_count)
    if finger.read_sysparam() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to get system parameters")
    if get_fingerprint():
           a=1
    else:
           a=0
    print("salida",a)
    
    if get_movement():
        b=1
    else:
        b=0
    print("salida",b)



