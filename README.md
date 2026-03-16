# Audio-Frequency-Analyzer

Python script that records live audio and analyzes it in the frequency domain using FFT. Plots the time-domain signal, frequency spectrum, and identifies the fundamental frequency and second harmonic. Built for the Señales y Sistemas course — UNAM Facultad de Ingeniería.

---

## What it does

1. Records 5 seconds of audio from the microphone.
2. Plots the signal in the **time domain**.
3. Computes the **FFT** and plots the frequency spectrum (0–6000 Hz).
4. Identifies and marks the **fundamental frequency** and the **second harmonic**.
5. Prints both frequency values to the console.

---

## Requirements

Python 3 and the following libraries:

```
pip install sounddevice numpy matplotlib
```

| Library | Purpose |
|---------|---------|
| `sounddevice` | Record audio from the microphone |
| `numpy` | FFT computation and array operations |
| `matplotlib` | Plot time-domain signal and frequency spectrum |

> On some systems, `sounddevice` also requires **PortAudio**. If you get an error on install, run:
> - **Windows:** usually works out of the box
> - **macOS:** `brew install portaudio`
> - **Linux:** `sudo apt install libportaudio2`

---

## Usage

```bash
python parte1.py
```

The script will prompt you in the console when recording starts and ends. Make sure your microphone is connected and set as the default input device.

---

## Output

- A plot of the audio signal in the time domain.
- A frequency spectrum with the fundamental frequency and second harmonic marked.
- Console output with both frequency values in Hz.

---

## Notes

- Sample rate is set to 16000 Hz and recording duration to 5 seconds. Both can be adjusted at the top of the script (`fs` and `duration` variables).
- The frequency spectrum is limited to 6000 Hz, which is sufficient for most voice and instrument analysis at this sample rate.
