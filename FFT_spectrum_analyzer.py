import numpy as np
import tkinter as tk
from tkinter import filedialog as fd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from scipy.io import wavfile
import scipy
import scipy.fftpack
import ntpath

def sine_wave(frame, f, fs, phase, ncyl):
    f = float(f.replace(",",".").replace("\n",""))
    fs = float(fs.replace(",",".").replace("\n",""))
    if (len(phase) == 0):
        phase = 0
    else:
        phase = float(phase.replace(",",".").replace("\n",""))
    ncyl = float(ncyl.replace(",",".").replace("\n",""))
    t = np.arange(0, ncyl*1/f, 1/fs)
    s = np.sin(2*np.pi*f*t+phase)
    # Write sine function to string
    if phase !=0:
        name = 'sin(2*π*'+str(f)+'+'+str(phase)+')'
    else:
        name = 'sin(2*π*'+str(f)+')'
    fft_fun(frame, s, fs, name)

def select_file(frame):
    filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',)
    samplerate, data = wavfile.read(filename)
    if (data.ndim > 1): #If file is stereo take only the first channel
        data = data[:,0]
    fft_fun(frame, data, samplerate,ntpath.basename(filename))

def fft_fun(frame, data, samplerate, name):
    fft = scipy.fft.fft(data)
    length = len(fft)
    fft = fft[:length//2] # one side of FFT
    ts = 1/samplerate # sample period
    t = [i*ts for i in range(len(data))] # time array for audio in time domain
    freq = scipy.fftpack.fftfreq(data.size, ts) # frequency array for frequency domain plot
    freq = freq[:len(freq)//2] # Takes one side of the frequency domain as well
    # Plot with matlibplot:
    fig = plt.Figure(figsize=(5,4), dpi = 100)
    ax1 = fig.add_subplot(211)
    ax1.plot(t,data)
    ax1.set_xlabel('Time (s)')
    ax1.set_title(name)
    ax2 = fig.add_subplot(212)
    ax2.stem(freq,2.0*abs(fft)/length)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_title('FFT')
    fig.subplots_adjust(hspace=1)

    # Delete previous plot
    for widget in frame.winfo_children():
        widget.destroy()
    # Place widgets
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
    toolbar.update()
    canvas.mpl_connect("key_press_event", lambda event: print(f"You pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def main():
    root = tk.Tk()
    root.title("FFT Spectrum Analyzer")

    title_frame = tk.Frame(root)
    title_frame.pack(fill='both', side = tk.TOP)
    title = tk.Label(title_frame,text="FFT Spectrum Analyzer")
    title.pack()
    title.configure(font=("Lucida Console", 40))
    frame1 = tk.Frame(root)
    frame1.pack(fill='both', side = tk.TOP)
    open_label = tk.Label(frame1, text="Choose a .wav file:", font=20)
    open_label.pack(side=tk.LEFT, anchor = 'e', expand=True)
    open_button = tk.Button(frame1,text='Open File', font=20,command=lambda: select_file(frame))
    open_button.pack(side=tk.RIGHT, anchor='w', expand=True)

    or_label = tk.Label(root, text="OR:", font=20)
    or_label.pack()
    frame2 = tk.Frame(root)
    frame2.pack(fill='both', side = tk.TOP)
    labeltext = tk.Label(frame2, text="Choose sine wave parameters:", font=16)
    labeltext.pack(sid=tk.LEFT, anchor = 'e', expand=True)
    labelf = tk.Label(frame2, text="Frequency (hz):", font=16)
    labelf.pack(sid=tk.LEFT, anchor = 'e')
    textf = tk.Text(frame2, height=1, width = 10)
    textf.pack(sid=tk.LEFT, anchor = 'e')
    labelphase = tk.Label(frame2, text="Phase (rad):", font=16)
    labelphase.pack(sid=tk.LEFT, anchor = 'e')
    textphase = tk.Text(frame2, height=1, width = 10)
    textphase.pack(sid=tk.LEFT, anchor = 'e')
    labelfs = tk.Label(frame2, text="Sample Frequency (hz):", font=16)
    labelfs.pack(sid=tk.LEFT, anchor = 'e')
    textfs = tk.Text(frame2, height=1, width = 10)
    textfs.pack(sid=tk.LEFT, anchor = 'e')
    labelncyl = tk.Label(frame2, text="Number of cycles:", font=16)
    labelncyl.pack(sid=tk.LEFT, anchor = 'e')
    textncyl = tk.Text(frame2, height=1, width = 10)
    textncyl.pack(sid=tk.LEFT, anchor = 'e')
    open_button = tk.Button(frame2,text='Calculate FFT', font=16, 
            command=lambda: sine_wave(
                    frame, textf.get('1.0', 'end-1c'), 
                    textfs.get('1.0', 'end-1c'), 
                    textphase.get('1.0', 'end-1c'), 
                    textncyl.get('1.0', 'end-1c')))
    open_button.pack(side=tk.RIGHT, anchor='w', expand=True)

    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    button = tk.Button(master=root, text="Quit", command=root.quit)
    button.pack(side=tk.BOTTOM)

    root.mainloop()


if __name__ == '__main__':
    main()