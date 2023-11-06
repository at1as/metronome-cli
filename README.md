# Metronome

Metronome is a command-line application that provides a simple way to create a metronome with adjustable BPM (beats per minute) and time signature.

## Features

- Adjust the BPM to set the metronome speed.
- Specify the time signature as "*/4" (e.g., 2/4, 3/4, 4/4, etc.).
- Visual representation of beats using '*' characters.
- Audible tick sound.
- Graceful exit handling with Ctrl+C.

## Requirements

- Python 3.x
- Sounddevice library (install with `pip install sounddevice`)
- Termcolor library (install with `pip install termcolor`)

## Usage

To start the metronome, run the following command:

python3 metronome <beats_per_minute> [time_signature]

- `<beats_per_minute>`: The desired BPM for the metronome.
- `[time_signature]`: (Optional) The time signature in the "*/4" format (e.g., 2/4, 3/4, 4/4). Default is 4/4.

Example:

```shell
$ python3 metronome 240 3/4


🎼 Metronome Started at 240 BPM in 3/4 time signature. Press Ctrl+C to exit.

[ *  *  * ]^C

Metronome stopped after 18 ticks. Duration: 7.15 seconds.
Effective BPM: 150
```

### Known Issues

* Built for macOS
* The effective BPM does match the input. It will scale relative to the input, however processing time for the script seems to be skewing things. Probably better to move the tick processing to a subprocess and do the other calculations in the main thread


