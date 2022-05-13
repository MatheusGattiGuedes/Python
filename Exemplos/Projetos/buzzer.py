from gpiozero import Buzzer
from signal import pause

buzzer = Buzzer(21)

buzzer.beep(1,1)

pause()
