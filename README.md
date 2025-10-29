# 🚦 ESP8266 Push Button LED Toggle using Interrupt (MicroPython)

This project demonstrates how to use **external interrupts** on the **ESP8266** to toggle an LED using a **push button**.  
Instead of continuously checking button state, the program reacts instantly when the button is pressed — making it more efficient and responsive.

---

## 🧠 Project Overview

| Component | Description |
|------------|-------------|
| **Board** | ESP8266 |
| **IDE** | Thonny IDE |
| **Language** | MicroPython |
| **USB Driver** | Silicon Labs CP210x USB to UART Bridge |
| **LED Pin** | GPIO2 |
| **Button Pin** | GPIO0 (Active LOW) |

---

## ⚙️ Requirements

- ESP8266 (NodeMCU or compatible)  
- 1 LED + 220Ω resistor  
- 1 Push Button  
- Micro USB cable  
- [Thonny IDE](https://thonny.org/)  
- [CP210x USB Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)  
- MicroPython firmware installed on ESP8266  

---

## 🧩 Circuit Connections

| ESP8266 Pin | Component | Description |
|--------------|------------|--------------|
| GPIO2 | LED | Output (Active LOW) |
| GPIO0 | Push Button | Input (Active LOW) |
| GND | LED (-) and Button GND | Common Ground |

💡 **Tip:** Use a pull-up resistor or internal pull-up on GPIO0 to prevent floating input issues.

---

## 💻 Code

```python
import machine

# GPIO2 = one LED connected
# GPIO0 = pushbutton

led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN)

def button_function(pin):
    led.value(not led.value())  # Toggle LED state

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_function)
