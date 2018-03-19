from src.properties_util import PropertyUtil
from gpiozero import LED


class LEDStatus:
    failed_LED = LED
    success_LED = LED
    building_LED = LED

    def __init__(self):
        led_config = (PropertyUtil().get_int("gpio", "pin"))['led']
        LEDStatus.success_LED = LED(led_config['success'])
        LEDStatus.failed_LED = LED(led_config['failed'])
        LEDStatus.building_LED = LED(led_config['building'])

    def mark_fail(self):
        LEDStatus.failed_LED.on()
        LEDStatus.success_LED.off()

    def mark_success(self):
        LEDStatus.success_LED.on()
        LEDStatus.failed_LED.off()

    def mark_building(self):
        LEDStatus.building_LED.blink(0.5, 0.5, background=True)

    def mark_building_stop(self):
        LEDStatus.building_LED.off()
