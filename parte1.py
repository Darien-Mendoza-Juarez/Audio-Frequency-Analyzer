import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# --- Grabamos audio ---
fs = 16000  # Frecuencia de muestreo
duration = 5  # segundos
print("Inicio grabación de entrada de audio...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
sd.wait()  # Espera a que termine
print("Fin de grabación de entrada de audio")

# --- Vector de tiempo ---
audio_data = audio.flatten()
t = np.arange(len(audio_data)) / fs

# --- Señal en el dominio del tiempo ---
plt.figure()
plt.plot(t, audio_data, '-r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal de audio en el dominio del tiempo')
plt.show()

# --- FFT ---
y_fft = np.abs(np.fft.fft(audio_data))
f = np.fft.fftfreq(len(y_fft), 1/fs)

# Nos quedamos con la mitad positiva del espectro
half = len(f)//2
f = f[:half]
y_fft = y_fft[:half]

# --- Espectro ---
plt.figure()
plt.plot(f, y_fft)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Espectro de Frecuencias')
plt.xlim([0, 6000])

# --- Frecuencia fundamental ---
ind_FrecFunda = np.argmax(y_fft)
frec_Funda = f[ind_FrecFunda]
seg_armonico = frec_Funda * 2
inx_armonico = (np.abs(f - seg_armonico)).argmin()

# --- Marcar en la gráfica ---
plt.plot(frec_Funda, y_fft[ind_FrecFunda], 'b.', markersize=12, label='Frecuencia fundamental')
plt.plot(seg_armonico, y_fft[inx_armonico], 'r.', markersize=12, label='Segundo Armónico')
plt.legend()
plt.show()

# --- Mostrar resultados ---
print("Frecuencias obtenidas:")
print(f"Frecuencia fundamental: {frec_Funda:.2f} Hz")
print(f"Frecuencia del armónico: {seg_armonico:.2f} Hz")
