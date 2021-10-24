# FFT Spectrum Analyzer
 FFT Spectrum Analyzer with a GUI in Python.
#### Description:
This project is a simple Python program that computes the [Fast Fourier Transform] (FFT) of a .wav file or a sine wave defined by the user. Users can define the frequency, phase, sample frequency and number of cycles of the sine wave.
It uses the tkinter framework to build a GUI, Scipy to calculate the FFT and it embeds Matplotlib charts in the GUI. This program plots two charts for the signal (audio file or sine wave): a time-domain graph of the input and the single-sided frequency spectrum calculated by the FFT of the signal.
Required modules can be installed with `pip install -r requirements.txt`. This program was created as my final project for the CS50X course.
This program can be useful for Electrical Engineering or related fields students to visualize some concepts of digital signal processing.
Below there are some usage examples.

## Analyzing .wav file

Click "Open file" and choose a .wav file on your computer. The top chart is the audio file plotted in the time domain, and the bottom chart is the FFT of the audio file, where the horizontal axis displays frequency in Hertz.
![Opening .wav file](/images/wav_file.PNG)

## Visualizing Aliasing example

This program can be used to visualize what is the [aliasing] phenomenon, which happens when a signal is sampled at a rate lower than two times its maximum frequency.

In the example below, a sine wave of frequency equals to 10 Hz is sampled with a sampling frequency of 16 Hz.
The successive cycles of the spectrum overlap with each other, so it appears that there is a component at 16-10=6 Hz, which does not exist in the sampled wave.

![Aliasing example](/images/aliasing.PNG)

## Visualizing Leakage example
[Leakage] is a distortion in the frequency spectrum that occurs when the measured signal is not periodic in the sample interval.

In the example below, a 10 Hz sine wave was sampled for 10.5 cycles, with a sampling frequency of 100 Hz. Because the FFT "assumes" the signal repeats itself after the interval, it doesn't "look" periodic, leading to leakage distortion.

![Leakage example](/images/leakage.PNG)

Whereas when we analyze the same sine wave but with exactly 10 cycles, there is no leakage distortion:

![No leakage example](/images/no_leakage.PNG)

[Window functions] are used to reduce leakage distortion, but they cannot eliminate it completely. They make the leakage distortion affect a smaller frequency range.

## Other details
- To add a phase shift to the sine wave function, you need to input a phase in radians. Also, frequencies should be in Hertz.
- If the .wav file has two channels, only the first one is used.

[Fast Fourier Transform]: <https://en.wikipedia.org/wiki/Fast_Fourier_transform>

[aliasing]: <https://en.wikipedia.org/wiki/Aliasing>

[Leakage]: <https://en.wikipedia.org/wiki/Spectral_leakage>

[Window functions]: <https://en.wikipedia.org/wiki/Window_function>