import time

import matplotlib.pyplot as plt
import numpy
import pyaudio
import scipy


def record():
    p = pyaudio.PyAudio()
    print("running")
    stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                    input=True, frames_per_buffer=FRAMESIZE)
    d = stream.read(NOFFRAMES * FRAMESIZE)
    decoded = numpy.frombuffer(d, numpy.int16)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("done")
    return decoded


def trigger(data_arr, threshold):
    for j, dp in enumerate(data_arr):
        if numpy.abs(dp) > threshold:
            return data_arr[j:j + SAMPLEFREQ]
    return []


def do_record():
    for j in range(0, 5):
        time.sleep(2)
        print("ready for run ", j)
        rec = record()
        numpy.save(f"recorded/a1/{j}.npy", rec)
        numpy.save(f"recorded/a1/{j}_trigger.npy", trigger(rec, 2000))
        print("2s pause")


def windowing(signal):
    window_size = 512
    window_overlap = window_size // 2  # int division
    gauss_window = scipy.signal.windows.gaussian(window_size, window_size / 4)

    windows = [
        numpy.concatenate(
            (numpy.zeros(x), signal[x:x + window_size] * gauss_window, numpy.zeros(len(signal) - x))
        ) for x in range(0, len(signal) - window_size, window_overlap)
    ]

    ft = [numpy.fft.fft(w) for w in windows]
    mean_ft = numpy.array(ft).mean(axis=0)
    ft_spec = numpy.abs(mean_ft)
    return ft_spec


FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220

if __name__ == '__main__':

    # do_record()

    for i in range(0, 5):
        print(i)
        data = numpy.load(f"recorded/a1/{i}.npy")
        data_trigger = numpy.load(f"recorded/a1/{i}_trigger.npy")

        # a + b
        fig, ax = plt.subplots()
        ax.plot(data)
        start_index = numpy.where(data == data_trigger[0])[0][0]
        ax.plot(numpy.arange(start_index, start_index + len(data_trigger)), data_trigger)
        ax.set_title(f"reference {i}")

        fig.savefig(f"plots/{i}.png")
        fig.show()

        # c
        fourier = numpy.fft.fft(data_trigger)
        spectrum = numpy.abs(fourier)

        plt.plot(range(len(spectrum)), spectrum)
        plt.title(f'amplitude spectrum without windowing : reference {i}')
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Amplitude in V')
        plt.grid(True)
        plt.savefig(f'plots/plot_spectrum_{i}.png')
        plt.show()

        # d
        w_ft = windowing(data_trigger)
        plt.plot(w_ft, 'g')
        plt.title(f'amplitude spectrum with windowing : reference {i}')
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Amplitude in V')
        plt.grid(True)
        plt.savefig(f'plots/plot_windowing_spectrum_{i}.png')
        plt.show()

