#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in February 2021
# Cycles RGB colours


import board
import digitalio
import time

import constants


def main():
    # Loops RGB from the LED

    redled = digitalio.DigitalInOut(board.D13)
    greenled = digitalio.DigitalInOut(board.D12)
    blueled = digitalio.DigitalInOut(board.D11)
    redled.direction = digitalio.Direction.OUTPUT
    greenled.direction = digitalio.Direction.OUTPUT
    blueled.direction = digitalio.Direction.OUTPUT

    while True:
        # Red
        redled.value = True
        time.sleep(constants.BLINK_TIME)
        redled.value = False
        time.sleep(constants.DELAY_TIME)

        # Green
        greenled.value = True
        time.sleep(constants.BLINK_TIME)
        greenled.value = False
        time.sleep(constants.DELAY_TIME)

        # Blue
        blueled.value = True
        time.sleep(constants.BLINK_TIME)
        blueled.value = False
        time.sleep(constants.DELAY_TIME)

        # Red-Green
        redled.value = True
        greenled.value = True
        time.sleep(constants.BLINK_TIME)
        redled.value = False
        greenled.value = False
        time.sleep(constants.DELAY_TIME)

        # Green-Blue
        greenled.value = True
        blueled.value = True
        time.sleep(constants.BLINK_TIME)
        greenled.value = False
        blueled.value = False
        time.sleep(constants.DELAY_TIME)

        # Blue-Red
        blueled.value = True
        redled.value = True
        time.sleep(constants.BLINK_TIME)
        blueled.value = False
        redled.value = False
        time.sleep(constants.DELAY_TIME)

        # Red-Green-Blue
        redled.value = True
        greenled.value = True
        blueled.value = True
        time.sleep(constants.BLINK_TIME)
        redled.value = False
        greenled.value = False
        blueled.value = False
        time.sleep(constants.DELAY_TIME)


if __name__ == "__main__":
    main()
