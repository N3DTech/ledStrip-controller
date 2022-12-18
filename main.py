'''
A simple WS2812b LED-Strip controller (single color, RGB code)
v1
© 2022, Markus Niemann

'''
import machine, neopixel


try:
      ledNumber = 14                                  # Number of PINs used      
      ledPin = 2                                      # GPIO of the microcontroller (my example D4, D1 mini) 

      ledStrip = neopixel.NeoPixel(machine.Pin(ledPin), ledNumber)

      for i in range(ledNumber):
            ledStrip[i] = (255, 0, 0)                 # LED color in RGB code
      ledStrip.write()
except:
      print('FAULT')
