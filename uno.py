import Adafruit_BBIO.ADC as ADC

pin_analogico = "P9_40"
ADC.setup()

def leer_tension(pin):
    
    valor_analogico = ADC.read(pin)
    voltaje = valor_analogico * 1.8  # rango de 0-1.8V

    return voltaje

while True:
    tension = leer_tension(pin_analogico)
    print("Tensión: {:.2f} V".format(tension))