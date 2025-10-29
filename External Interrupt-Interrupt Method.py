import machine
#GPIO2 = one LED connected
#GPIO0 = pushbutton
led = machine.Pin(2,machine.Pin.OUT)
button = machine.Pin(0,machine.Pin.IN)

def button_function(pin):
    led.value(not led.value()) #toggling of LED GPIO2
    
button.irq(trigger=machine.Pin.IRQ_FALLING,handler=button_function)