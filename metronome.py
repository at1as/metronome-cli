#!/usr/bin/env python

import sys
import time
import sounddevice as sd
import numpy as np
from termcolor import colored

TICK_SEPARATOR = " * "
TICK_WIDTH = len(TICK_SEPARATOR)

def metronome(bpm, time_signature):
    if bpm <= 0:
        print("Please provide a positive BPM value.")
        return

    tick_duration = 0.05  # TODO: Adjust this value based on your input BPM. Value in seconds

    if time_signature.endswith("/4"):
        try:
            numerator = int(time_signature.split("/")[0])
            if 1 <= numerator <= 20:
                ticks_per_measure = numerator
                visual_width = numerator  # Adjust the width based on the time signature
            else:
                numerator = 4  # Default to 4 in case of an invalid numerator
                ticks_per_measure = 4
                visual_width = 4
                print("Invalid numerator. Defaulting to 4/4 time signature.")
        except ValueError:
            numerator = 4  # Default to 4 in case of parsing errors
            ticks_per_measure = 4
            visual_width = 4
            print("Invalid time signature format. Defaulting to 4/4 time signature.")
    else:
        numerator = 4  # Default to 4 in case of parsing errors
        time_signature = "4/4"
        ticks_per_measure = 4
        visual_width = 4
        print("Unsupported time signature format. Defaulting to 4/4 time signature (only */4 time signatures are supported).")

    interval = (60.0 / bpm) - tick_duration  # Calculate the interval between ticks

    def play_tick_sound():
        # Play a beep sound
        frequency = 440  # Adjust this value for the desired tick sound frequency
        amplitude = 0.5
        t = np.linspace(0, tick_duration, int(44100 * tick_duration), False)
        tick_sound = amplitude * np.sin(2 * np.pi * frequency * t)
        sd.play(tick_sound)
        sd.wait()

    try:
        print("\n🎼" + colored(f" Metronome ", 'red') + "Started at " + colored(f"{bpm} BPM", 'green') + " in " + colored(time_signature, 'green') + " time signature. Press Ctrl+C to exit." + "\n")
        tick_count = 1
        total_tick_count = 1
        start_time = time.time()  # Record the start time

        while True:
            visual = TICK_SEPARATOR * tick_count
            adjusted_visual_width = visual_width * TICK_WIDTH
            print(f"\r[{visual:<{adjusted_visual_width}}]", end="", flush=True)

            tick_count = (tick_count % ticks_per_measure) + 1
            total_tick_count += 1;
            play_tick_sound()
            time.sleep(interval)
    except KeyboardInterrupt:
        end_time = time.time()  # Record the end time
        duration = end_time - start_time  # Calculate the duration
        print(f"\n\nMetronome stopped after {total_tick_count - 1} ticks. Duration: {duration:.2f} seconds.")
        print(f"Effective BPM: {int((total_tick_count - 1) / (duration / 60))}")
        sd.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./metronome <beats_per_minute> [time_signature]")
    else:
        try:
            bpm = int(sys.argv[1])
            time_signature = "4/4" if len(sys.argv) < 3 else sys.argv[2]
            metronome(bpm, time_signature)
        except ValueError:
            print("Invalid BPM value. Please provide an integer.")

