from src.properties_util import PropertyUtil
from gpiozero import LED


class LEDStatus:
    failed_LED: LED
    success_LED: LED
    building_LED: LED

    def __init__(self):
        LEDStatus.success_LED = PropertyUtil().get_int("rapberry_gpio_config", "gpio.job.success.led.pin")
        LEDStatus.fail_LED = PropertyUtil().get_int("rapberry_gpio_config", "gpio.job.failed.led.pin")
        LEDStatus.building_LED = PropertyUtil().get_int("rapberry_gpio_config", "gpio.job.building.led.pin")

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
