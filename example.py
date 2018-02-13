from ut61 import Ut61

multimeter = Ut61(convertValues=True)
unit = multimeter.currentReading["unit"] 
amps = multimeter.currentReading["value"i]
