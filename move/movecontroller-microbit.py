from microbit import *

deadzone_x = 200
deadzone_y = 200

def get_sensor_data():
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    a, b = button_a.was_pressed(), button_b.was_pressed()
    print(x, y, z, a, b)
    return x, y

while True:
    sleep(100)
    x, y = get_sensor_data()
    # Display direction output. For reasons I don't understand, this only works properly for 'S'.
    if int(x) < ( 0 - deadzone_x ):
        display.show("A", wait=False)
    if int(x) > deadzone_x:
        display.show("D", wait=False)
    if int(y) < (0 - deadzone_y):
        display.show("W", wait=False)
    if int(y) > deadzone_y:
        display.show("S", wait=False)
    else:
        display.show(" ", wait=False)