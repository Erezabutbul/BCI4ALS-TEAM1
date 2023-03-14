import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.fft import rfft, rfftfreq
pd.options.mode.chained_assignment = None  # default='warn'

sns.set(rc={'figure.figsize': (5, 3)})


def plot_per_electrode_time_domain(df, str):
    fig, ax = plt.subplots(16,1)
    t = np.arange(0, (1/fs) * len(df['channel_1']), (1/fs))
    ax[0].plot(t, df['channel_1'], label='Electrode 1', color="#f0e594")
    ax[0].legend(loc="right")
    #ax[0].set(ylabel='Voltage [mV]')
    ax[1].plot(t, df['channel_2'], label='Electrode 2', color="#57b884")
    ax[1].legend(loc="right")
    #ax[1].set(xlabel='Time [Seconds]')
    ax[2].plot(t, df['channel_3'], label='Electrode 3', color="#ffab8d")
    ax[2].legend(loc="right")
    #ax[2].set(xlabel='Time [Seconds]')
    ax[3].plot(t, df['channel_4'], label='Electrode 4', color="#f2cbac")
    ax[3].legend(loc="right")
    #ax[3].set(xlabel='Time [Seconds]')
    ax[4].plot(t, df['channel_5'], label='Electrode 5', color="#f0e594")
    ax[4].legend(loc="right")
    #ax[4].set(ylabel='Voltage [mV]', xlabel='Time [Seconds]')
    ax[5].plot(t, df['channel_6'], label='Electrode 6', color="#57b884")
    ax[5].legend(loc="right")
    #ax[5].set(xlabel='Time [Seconds]')
    ax[6].plot(t, df['channel_7'], label='Electrode 7', color="#ffab8d")
    ax[6].legend(loc="right")
    #ax[6].set(xlabel='Time [Seconds]')
    ax[7].plot(t, df['channel_8'], label='Electrode 8', color="#f2cbac")
    ax[7].legend(loc="right")
    #ax[7].set(xlabel='Time [Seconds]')
    ax[8].plot(t, df['channel_9'], label='Electrode 9', color="#f0e594")
    ax[8].legend(loc="right")
    ax[8].set(ylabel='Voltage [mV]')
    ax[9].plot(t, df['channel_10'], label='Electrode 10', color="#57b884")
    ax[9].legend(loc="right")
    #ax[9].set(xlabel='Time [Seconds]')
    ax[10].plot(t, df['channel_11'], label='Electrode 11', color="#ffab8d")
    ax[10].legend(loc="right")
    #ax[10].set(xlabel='Time [Seconds]')
    ax[11].plot(t, df['channel_12'], label='Electrode 12', color="#f2cbac")
    ax[11].legend(loc="right")
    #ax[11].set(xlabel='Time [Seconds]')
    ax[12].plot(t, df['channel_13'], label='Electrode 13', color="#f0e594")
    ax[12].legend(loc="right")
    #ax[12].set(ylabel='Voltage [mV]', xlabel='Time [Seconds]')
    ax[13].plot(t, df['channel_14'], label='Electrode 14', color="#57b884")
    ax[13].legend(loc="right")
    #ax[13].set(xlabel='Time [Seconds]')
    ax[14].plot(t, df['channel_15'], label='Electrode 15', color="#ffab8d")
    ax[14].legend(loc="right")
    #ax[14].set(xlabel='Time [Seconds]')
    ax[15].plot(t, df['channel_16'], label='Electrode 16', color="#f2cbac")
    ax[15].legend(loc="right")
    ax[15].set(xlabel='Time [Seconds]')
    if str == "raw":
        fig.suptitle("""EEG Raw Data Per Electrode  - Time Domain\n\n""", fontweight="bold")
    else:
        fig.suptitle("""EEG Filtered Data Per Electrode\n\n""", fontweight="bold")


def plot_per_electrode_frequency_domain(df, str):
    yf1 = rfft(df['channel_1'].values)
    yf2 = rfft(df['channel_2'].values)
    yf3 = rfft(df['channel_3'].values)
    yf4 = rfft(df['channel_4'].values)
    yf5 = rfft(df['channel_5'].values)
    yf6 = rfft(df['channel_6'].values)
    yf7 = rfft(df['channel_7'].values)
    yf8 = rfft(df['channel_8'].values)
    yf9 = rfft(df['channel_9'].values)
    yf10 = rfft(df['channel_10'].values)
    yf11 = rfft(df['channel_11'].values)
    yf12 = rfft(df['channel_12'].values)
    yf13 = rfft(df['channel_13'].values)
    yf14 = rfft(df['channel_14'].values)
    yf15 = rfft(df['channel_15'].values)
    N = df.shape[0]  # number of rows - samples
    xf = rfftfreq(N, 1 / fs)

    fig, ax = plt.subplots()

    ax.plot(xf, abs(yf1), label='Electrode 1')
    ax.plot(xf, abs(yf2), label='Electrode 2')
    ax.plot(xf, abs(yf3), label='Electrode 3')
    ax.plot(xf, abs(yf4), label='Electrode 4')
    ax.plot(xf, abs(yf5), label='Electrode 5')
    ax.plot(xf, abs(yf6), label='Electrode 6')
    ax.plot(xf, abs(yf7), label='Electrode 7')
    ax.plot(xf, abs(yf8), label='Electrode 8')
    ax.plot(xf, abs(yf9), label='Electrode 9')
    ax.plot(xf, abs(yf10), label='Electrode 10')
    ax.plot(xf, abs(yf11), label='Electrode 11')
    ax.plot(xf, abs(yf12), label='Electrode 12')
    ax.plot(xf, abs(yf13), label='Electrode 13')
    ax.plot(xf, abs(yf14), label='Electrode 14')
    ax.plot(xf, abs(yf15), label='Electrode 15')
    ax.legend()
    plt.ylim(0, 500000)
    ax.set(xlabel='Frequency [Hz]', ylabel='Amplitude')
    if str == "raw":
        fig.suptitle("""EEG Raw Data Per Electrode  - Frequency Domain\n\n""", fontweight="bold")
    else:
        fig.suptitle("""EEG Filtered Data Per Electrode  - Frequency Domain\n\n""", fontweight="bold")


def plot_erp_per_electrode_time_domain(baseline, distractor, target):
    baseline = baseline.T
    distractor = distractor.T
    target = target.T
    event_time = 0.2
    fig, ax = plt.subplots(4, 4)
    t = np.arange(0, (1/fs) * len(baseline[2][1:-1]), (1/fs))
    ax[0, 0].plot(t, baseline[2][1:-1], label='Baseline', color="#f0e594")
    ax[0, 0].plot(t, distractor[2][1:-1], label='Distractor', color="#57b884")
    ax[0, 0].plot(t, target[2][1:-1], label='Target', color="#ffab8d")
    ax[0, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 0].legend(loc="upper left")
    ax[0, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 0].title.set_text('Electrode 1')

    ax[1, 0].plot(t, baseline[3][1:-1], label='Baseline', color="#f0e594")
    ax[1, 0].plot(t, distractor[3][1:-1], label='Distractor', color="#57b884")
    ax[1, 0].plot(t, target[3][1:-1], label='Target', color="#ffab8d")
    ax[1, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 0].legend(loc="upper left")
    ax[1, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 0].title.set_text('Electrode 2')

    ax[2, 0].plot(t, baseline[4][1:-1], label='Baseline', color="#f0e594")
    ax[2, 0].plot(t, distractor[4][1:-1], label='Distractor', color="#57b884")
    ax[2, 0].plot(t, target[4][1:-1], label='Target', color="#ffab8d")
    ax[2, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 0].legend(loc="upper left")
    ax[2, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 0].title.set_text('Electrode 3')

    ax[3, 0].plot(t, baseline[5][1:-1], label='Baseline', color="#f0e594")
    ax[3, 0].plot(t, distractor[5][1:-1], label='Distractor', color="#57b884")
    ax[3, 0].plot(t, target[5][1:-1], label='Target', color="#ffab8d")
    ax[3, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 0].legend(loc="upper left")
    ax[3, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 0].title.set_text('Electrode 4')

    ax[0, 1].plot(t, baseline[6][1:-1], label='Baseline', color="#f0e594")
    ax[0, 1].plot(t, distractor[6][1:-1], label='Distractor', color="#57b884")
    ax[0, 1].plot(t, target[6][1:-1], label='Target', color="#ffab8d")
    ax[0, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 1].legend(loc="upper left")
    ax[0, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 1].title.set_text('Electrode 5')

    ax[1, 1].plot(t, baseline[7][1:-1], label='Baseline', color="#f0e594")
    ax[1, 1].plot(t, distractor[7][1:-1], label='Distractor', color="#57b884")
    ax[1, 1].plot(t, target[7][1:-1], label='Target', color="#ffab8d")
    ax[1, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 1].legend(loc="upper left")
    ax[1, 1].title.set_text('Electrode 6')
    ax[1, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')

    ax[2, 1].plot(t, baseline[8][1:-1], label='Baseline', color="#f0e594")
    ax[2, 1].plot(t, distractor[8][1:-1], label='Distractor', color="#57b884")
    ax[2, 1].plot(t, target[8][1:-1], label='Target', color="#ffab8d")
    ax[2, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 1].legend(loc="upper left")
    ax[2, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 1].title.set_text('Electrode 7')

    ax[3, 1].plot(t, baseline[9][1:-1], label='Baseline', color="#f0e594")
    ax[3, 1].plot(t, distractor[9][1:-1], label='Distractor', color="#57b884")
    ax[3, 1].plot(t, target[9][1:-1], label='Target', color="#ffab8d")
    ax[3, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 1].legend(loc="upper left")
    ax[3, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 1].title.set_text('Electrode 8')

    ax[0, 2].plot(t, baseline[10][1:-1], label='Baseline', color="#f0e594")
    ax[0, 2].plot(t, distractor[10][1:-1], label='Distractor', color="#57b884")
    ax[0, 2].plot(t, target[10][1:-1], label='Target', color="#ffab8d")
    ax[0, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 2].legend(loc="upper left")
    ax[0, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 2].title.set_text('Electrode 9')

    ax[1, 2].plot(t, baseline[11][1:-1], label='Baseline', color="#f0e594")
    ax[1, 2].plot(t, distractor[11][1:-1], label='Distractor', color="#57b884")
    ax[1, 2].plot(t, target[11][1:-1], label='Target', color="#ffab8d")
    ax[1, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 2].legend(loc="upper left")
    ax[1, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 2].title.set_text('Electrode 10')

    ax[2, 2].plot(t, baseline[12][1:-1], label='Baseline', color="#f0e594")
    ax[2, 2].plot(t, distractor[12][1:-1], label='Distractor', color="#57b884")
    ax[2, 2].plot(t, target[12][1:-1], label='Target', color="#ffab8d")
    ax[2, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 2].legend(loc="upper left")
    ax[2, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 2].title.set_text('Electrode 11')

    ax[3, 2].plot(t, baseline[13][1:-1], label='Baseline', color="#f0e594")
    ax[3, 2].plot(t, distractor[13][1:-1], label='Distractor', color="#57b884")
    ax[3, 2].plot(t, target[13][1:-1], label='Target', color="#ffab8d")
    ax[3, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 2].legend(loc="upper left")
    ax[3, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 2].title.set_text('Electrode 12')

    ax[0, 3].plot(t, baseline[14][1:-1], label='Baseline', color="#f0e594")
    ax[0, 3].plot(t, distractor[14][1:-1], label='Distractor', color="#57b884")
    ax[0, 3].plot(t, target[14][1:-1], label='Target', color="#ffab8d")
    ax[0, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 3].legend(loc="upper left")
    ax[0, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 3].title.set_text('Electrode 13')

    ax[1, 3].plot(t, baseline[15][1:-1], label='Baseline', color="#f0e594")
    ax[1, 3].plot(t, distractor[15][1:-1], label='Distractor', color="#57b884")
    ax[1, 3].plot(t, target[15][1:-1], label='Target', color="#ffab8d")
    ax[1, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 3].legend(loc="upper left")
    ax[1, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 3].title.set_text('Electrode 14')

    ax[2, 3].plot(t, baseline[16][1:-1], label='Baseline', color="#f0e594")
    ax[2, 3].plot(t, distractor[16][1:-1], label='Distractor', color="#57b884")
    ax[2, 3].plot(t, target[16][1:-1], label='Target', color="#ffab8d")
    ax[2, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 3].legend(loc="upper left")
    ax[2, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 3].title.set_text('Electrode 15')

    ax[3, 3].plot(t, baseline[17][1:-1], label='Baseline', color="#f0e594")
    ax[3, 3].plot(t, distractor[17][1:-1], label='Distractor', color="#57b884")
    ax[3, 3].plot(t, target[17][1:-1], label='Target', color="#ffab8d")
    ax[3, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 3].legend(loc="upper left")
    ax[3, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 3].title.set_text('Electrode 16')

    fig.suptitle("""EEG ERP Data Per Electrode  - Time Domain\n\n""", fontweight="bold")

def plot_erp_per_block_time_domain(block1, block2, block3, block4, block5):
    block1 = block1.T
    block2 = block2.T
    block3 = block3.T
    block4 = block4.T
    block5 = block5.T
    event_time = 0.2
    fig, ax = plt.subplots(4, 4)
    t = np.arange(0, (1/fs) * len(block5[2][1:-1]), (1/fs))
    ax[0, 0].plot(t, block1[0][1:-1], label='Block 1')
    ax[0, 0].plot(t, block2[0][1:-1], label='Block 2')
    ax[0, 0].plot(t, block3[0][1:-1], label='Block 3')
    ax[0, 0].plot(t, block4[0][1:-1], label='Block 4')
    ax[0, 0].plot(t, block5[0][1:-1], label='Block 5')
    ax[0, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 0].legend(loc="upper left")
    ax[0, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 0].title.set_text('Electrode 1')

    ax[1, 0].plot(t, block1[1][1:-1], label='Block 1')
    ax[1, 0].plot(t, block2[1][1:-1], label='Block 2')
    ax[1, 0].plot(t, block3[1][1:-1], label='Block 3')
    ax[1, 0].plot(t, block4[1][1:-1], label='Block 4')
    ax[1, 0].plot(t, block5[1][1:-1], label='Block 5')
    ax[1, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 0].legend(loc="upper left")
    ax[1, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 0].title.set_text('Electrode 2')

    ax[2, 0].plot(t, block1[2][1:-1], label='Block 1')
    ax[2, 0].plot(t, block2[2][1:-1], label='Block 2')
    ax[2, 0].plot(t, block3[2][1:-1], label='Block 3')
    ax[2, 0].plot(t, block4[2][1:-1], label='Block 4')
    ax[2, 0].plot(t, block5[2][1:-1], label='Block 5')
    ax[2, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 0].legend(loc="upper left")
    ax[2, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 0].title.set_text('Electrode 3')

    ax[3, 0].plot(t, block1[3][1:-1], label='Block 1')
    ax[3, 0].plot(t, block2[3][1:-1], label='Block 2')
    ax[3, 0].plot(t, block3[3][1:-1], label='Block 3')
    ax[3, 0].plot(t, block4[3][1:-1], label='Block 4')
    ax[3, 0].plot(t, block5[3][1:-1], label='Block 5')
    ax[3, 0].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 0].legend(loc="upper left")
    ax[3, 0].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 0].title.set_text('Electrode 4')

    ax[0, 1].plot(t, block1[4][1:-1], label='Block 1')
    ax[0, 1].plot(t, block2[4][1:-1], label='Block 2')
    ax[0, 1].plot(t, block3[4][1:-1], label='Block 3')
    ax[0, 1].plot(t, block4[4][1:-1], label='Block 4')
    ax[0, 1].plot(t, block5[4][1:-1], label='Block 5')
    ax[0, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 1].legend(loc="upper left")
    ax[0, 1].title.set_text('Electrode 5')
    ax[0, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')

    ax[1, 1].plot(t, block1[5][1:-1], label='Block 1')
    ax[1, 1].plot(t, block2[5][1:-1], label='Block 2')
    ax[1, 1].plot(t, block3[5][1:-1], label='Block 3')
    ax[1, 1].plot(t, block4[5][1:-1], label='Block 4')
    ax[1, 1].plot(t, block5[5][1:-1], label='Block 5')
    ax[1, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 1].legend(loc="upper left")
    ax[1, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 1].title.set_text('Electrode 6')

    ax[2, 1].plot(t, block1[6][1:-1], label='Block 1')
    ax[2, 1].plot(t, block2[6][1:-1], label='Block 2')
    ax[2, 1].plot(t, block3[6][1:-1], label='Block 3')
    ax[2, 1].plot(t, block4[6][1:-1], label='Block 4')
    ax[2, 1].plot(t, block5[6][1:-1], label='Block 5')
    ax[2, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 1].legend(loc="upper left")
    ax[2, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 1].title.set_text('Electrode 7')

    ax[3, 1].plot(t, block1[7][1:-1], label='Block 1')
    ax[3, 1].plot(t, block2[7][1:-1], label='Block 2')
    ax[3, 1].plot(t, block3[7][1:-1], label='Block 3')
    ax[3, 1].plot(t, block4[7][1:-1], label='Block 4')
    ax[3, 1].plot(t, block5[7][1:-1], label='Block 5')
    ax[3, 1].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 1].legend(loc="upper left")
    ax[3, 1].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 1].title.set_text('Electrode 8')

    ax[0, 2].plot(t, block1[8][1:-1], label='Block 1')
    ax[0, 2].plot(t, block2[8][1:-1], label='Block 2')
    ax[0, 2].plot(t, block3[8][1:-1], label='Block 3')
    ax[0, 2].plot(t, block4[8][1:-1], label='Block 4')
    ax[0, 2].plot(t, block5[8][1:-1], label='Block 5')
    ax[0, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 2].legend(loc="upper left")
    ax[0, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[0, 2].title.set_text('Electrode 9')

    ax[1, 2].plot(t, block1[9][1:-1], label='Block 1')
    ax[1, 2].plot(t, block2[9][1:-1], label='Block 2')
    ax[1, 2].plot(t, block3[9][1:-1], label='Block 3')
    ax[1, 2].plot(t, block4[9][1:-1], label='Block 4')
    ax[1, 2].plot(t, block5[9][1:-1], label='Block 5')
    ax[1, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 2].legend(loc="upper left")
    ax[1, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 2].title.set_text('Electrode 10')

    ax[2, 2].plot(t, block1[10][1:-1], label='Block 1')
    ax[2, 2].plot(t, block2[10][1:-1], label='Block 2')
    ax[2, 2].plot(t, block3[10][1:-1], label='Block 3')
    ax[2, 2].plot(t, block4[10][1:-1], label='Block 4')
    ax[2, 2].plot(t, block5[10][1:-1], label='Block 5')
    ax[2, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 2].legend(loc="upper left")
    ax[2, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 2].title.set_text('Electrode 11')

    ax[3, 2].plot(t, block1[11][1:-1], label='Block 1')
    ax[3, 2].plot(t, block2[11][1:-1], label='Block 2')
    ax[3, 2].plot(t, block3[11][1:-1], label='Block 3')
    ax[3, 2].plot(t, block4[11][1:-1], label='Block 4')
    ax[3, 2].plot(t, block5[11][1:-1], label='Block 5')
    ax[3, 2].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 2].legend(loc="upper left")
    ax[3, 2].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[3, 2].title.set_text('Electrode 12')

    ax[0, 3].plot(t, block1[12][1:-1], label='Block 1')
    ax[0, 3].plot(t, block2[12][1:-1], label='Block 2')
    ax[0, 3].plot(t, block3[12][1:-1], label='Block 3')
    ax[0, 3].plot(t, block4[12][1:-1], label='Block 4')
    ax[0, 3].plot(t, block5[12][1:-1], label='Block 5')
    ax[0, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[0, 3].legend(loc="upper left")
    ax[0, 3].title.set_text('Electrode 13')
    ax[0, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[1, 3].plot(t, block1[13][1:-1], label='Block 1')
    ax[1, 3].plot(t, block2[13][1:-1], label='Block 2')
    ax[1, 3].plot(t, block3[13][1:-1], label='Block 3')
    ax[1, 3].plot(t, block4[13][1:-1], label='Block 4')
    ax[1, 3].plot(t, block5[13][1:-1], label='Block 5')
    ax[1, 3].title.set_text('Electrode 14')

    ax[1, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[1, 3].legend(loc="upper left")
    ax[1, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 3].plot(t, block1[14][1:-1], label='Block 1')
    ax[2, 3].plot(t, block2[14][1:-1], label='Block 2')
    ax[2, 3].plot(t, block3[14][1:-1], label='Block 3')
    ax[2, 3].plot(t, block4[14][1:-1], label='Block 4')
    ax[2, 3].plot(t, block5[14][1:-1], label='Block 5')
    ax[2, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[2, 3].legend(loc="upper left")
    ax[2, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')
    ax[2, 3].title.set_text('Electrode 15')

    ax[3, 3].plot(t, block1[15][1:-1], label='Block 1')
    ax[3, 3].plot(t, block2[15][1:-1], label='Block 2')
    ax[3, 3].plot(t, block3[15][1:-1], label='Block 3')
    ax[3, 3].plot(t, block4[15][1:-1], label='Block 4')
    ax[3, 3].plot(t, block5[15][1:-1], label='Block 5')
    ax[3, 3].title.set_text('Electrode 16')
    ax[3, 3].vlines(event_time, color="red", ymin=-200, ymax=200)
    ax[3, 3].legend(loc="upper left")
    ax[3, 3].set(xlabel='Time [Seconds]', ylabel='Voltage [\u03BCV]')

directory = os.getcwd()
fs = 125
# Visualization of raw and post processing data

# Raw data

# Time Domain
EEG_raw = pd.read_csv(directory + "\\output_files\\EEG_Recordings\\EEG_Recording_unprocessed.csv")
plt.figure(0)
plot_per_electrode_time_domain(EEG_raw, "raw")




# Freqency domaim
plt.figure(1)
plot_per_electrode_frequency_domain(EEG_raw, "raw")


# Filtered data

# Time Domain
plt.figure(1)
EEG_filtered = pd.read_csv(directory + "\\output_files\\filtered_EEG_Recordings\\EEG_Recording_processed.csv")
plot_per_electrode_time_domain(EEG_filtered, "filtered")

# Frequency Domain
plot_per_electrode_frequency_domain(EEG_filtered, "filtered")



# On specific Electrode - 5
t5 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t5, EEG_raw['channel_5'], label='Electrode 5 - Before Filtering', color="black")
ax[1].plot(t5, EEG_filtered['channel_5'], label='Electrode 5 -  After Filtering', color="blue")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 4
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t4, EEG_raw['channel_4'], label='Electrode 4 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_4'], label='Electrode 4 -  After Filtering', color="green")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 2
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t4, EEG_raw['channel_2'], label='Electrode 2 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_2'], label='Electrode 2 -  After Filtering', color="purple")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 1
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t4, EEG_raw['channel_1'], label='Electrode 1 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_1'], label='Electrode 1 -  After Filtering', color="orange")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 3
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t4, EEG_raw['channel_3'], label='Electrode 3 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_3'], label='Electrode 3 -  After Filtering', color="red")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 6
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_6'], label='Electrode 6 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_6'], label='Electrode 6 -  After Filtering', color="c")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])
# On specific Electrode - 7
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1,2)
ax[0].plot(t4, EEG_raw['channel_7'], label='Electrode 7 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_7'], label='Electrode 7 -  After Filtering', color="maroon")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 8
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_8'], label='Electrode 8 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_8'], label='Electrode 8 -  After Filtering', color="deeppink")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])
# On specific Electrode - 9
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_9'], label='Electrode 9 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_9'], label='Electrode 9 -  After Filtering', color="teal")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])
# On specific Electrode - 10
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_10'], label='Electrode 10 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_10'], label='Electrode 10 -  After Filtering', color="deepskyblue")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 11
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_11'], label='Electrode 11 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_11'], label='Electrode 11 -  After Filtering', color="grey")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])

# On specific Electrode - 12
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_12'], label='Electrode 12 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_12'], label='Electrode 12 -  After Filtering', color="violet")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])
# On specific Electrode - 13
t4 = np.arange(0, (1 / fs) * len(EEG_raw['channel_1']), (1 / fs))
fig, ax = plt.subplots(1, 2)
ax[0].plot(t4, EEG_raw['channel_13'], label='Electrode 13 - Before Filtering', color="black")
ax[1].plot(t4, EEG_filtered['channel_13'], label='Electrode 13 -  After Filtering', color="gold")
ax[0].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[1].set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax[0].set(xlim=[155, 157])
ax[1].set(xlim=[155, 157])


# ERP Visualization

# Number of Repetition from each ERP
baseline_exp = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\baseLine_AVG_all_the_EXP.csv")
baseline_block1 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\AVG_block_num_0.csv")
baseline_block2 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\AVG_block_num_1.csv")
baseline_block3 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\AVG_block_num_2.csv")
baseline_block4 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\AVG_block_num_3.csv")
baseline_block5 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\baseLine\\Mean_EEG_Signal_baseLine\\AVG_block_num_4.csv")

distractor_exp = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\distractor_AVG_all_the_EXP.csv")
distractor_block1 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\AVG_block_num_0.csv")
distractor_block2 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\AVG_block_num_1.csv")
distractor_block3 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\AVG_block_num_2.csv")
distractor_block4 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\AVG_block_num_3.csv")
distractor_block5 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\distractor\\Mean_EEG_Signal_distractor\\AVG_block_num_4.csv")

target_exp = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\target_AVG_all_the_EXP.csv")
target_block1 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\AVG_block_num_0.csv")
target_block2 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\AVG_block_num_1.csv")
target_block3 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\AVG_block_num_2.csv")
target_block4 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\AVG_block_num_3.csv")
target_block5 = pd.read_csv(directory + "\\output_files\\cut_data_by_class\\target\\Mean_EEG_Signal_target\\AVG_block_num_4.csv")

# ERP per electrode
plot_erp_per_electrode_time_domain(baseline_exp, distractor_exp, target_exp)

# ERP per type per electrode across blocks
plot_erp_per_block_time_domain(baseline_block1, baseline_block2, baseline_block3, baseline_block4, baseline_block5)
plot_erp_per_block_time_domain(distractor_block1, distractor_block2, distractor_block3, distractor_block4, distractor_block5)
plot_erp_per_block_time_domain(target_block1, target_block2, target_block3, target_block4, target_block5)

# ERP Example
t = np.arange(0, (1 / fs) * len(baseline_exp.T[2][1:-1]), (1 / fs))
fig, ax = plt.subplots()
ax.plot(t, baseline_exp.T[11][1:-1], label='Electrode 10 - Baseline', color="#f0e594")
ax.plot(t, distractor_exp.T[11][1:-1], label='Electrode 10 - Distractor', color="#57b884")
ax.plot(t, target_exp.T[11][1:-1], label='Electrode 10 - Target', color="#ffab8d")
ax.set(ylabel='Voltage [\u03BCV]', xlabel='time [sec]')
ax.vlines(0.2, color="red", ymin=-200, ymax=200)
ax.vlines(0.5, color="blue", ymin=-200, ymax=200)
ax.legend(loc="upper left")
ax.set_ylim((-35, 50))
fig.suptitle("""EEG ERP Electrode 10  - Time Domain\n\n""", fontweight="bold")

fig, ax = plt.subplots()
ax.plot(t, baseline_exp.T[5][1:-1], label='Electrode 4 - Baseline', color="#f0e594")
ax.plot(t, distractor_exp.T[5][1:-1], label='Electrode 4 - Distractor', color="#57b884")
ax.plot(t, target_exp.T[5][1:-1], label='Electrode 4 - Target', color="#ffab8d")
ax.vlines(0.2, color="red", ymin=-200, ymax=200)
ax.vlines(0.5, color="blue", ymin=-200, ymax=200)
ax.legend(loc="upper left")
ax.set_ylim((-35, 50))
fig.suptitle("""EEG ERP Electrode 4  - Time Domain\n\n""", fontweight="bold")


fig, ax = plt.subplots()
ax.plot(t, baseline_exp.T[10][1:-1], label='Electrode 9 - Baseline', color="#f0e594")
ax.plot(t, distractor_exp.T[10][1:-1], label='Electrode 9 - Distractor', color="#57b884")
ax.plot(t, target_exp.T[10][1:-1], label='Electrode 9 - Target', color="#ffab8d")
ax.vlines(0.2, color="red", ymin=-200, ymax=200)
ax.vlines(0.5, color="blue", ymin=-200, ymax=200)
ax.legend(loc="upper left")
ax.set_ylim((-35, 50))
fig.suptitle("""EEG ERP Electrode 9  - Time Domain\n\n""", fontweight="bold")

fig, ax = plt.subplots()
ax.plot(t, baseline_exp.T[3][1:-1], label='Electrode 2 - Baseline', color="#f0e594")
ax.plot(t, distractor_exp.T[3][1:-1], label='Electrode 2 - Distractor', color="#57b884")
ax.plot(t, target_exp.T[3][1:-1], label='Electrode 2 - Target', color="#ffab8d")
ax.vlines(0.2, color="red", ymin=-200, ymax=200)
ax.vlines(0.5, color="blue", ymin=-200, ymax=200)
ax.legend(loc="upper left")
ax.set_ylim((-35, 50))
fig.suptitle("""EEG ERP Electrode 2  - Time Domain\n\n""", fontweight="bold")


# comparison before after filtering on the same electrode

# Feature space visualization
features = pd.read_csv(directory + "\\output_files\\featuresAndModels\\features\\featuresMatrix.csv")
labels = [[[["Target"], ["Distractor"]]*10]*8]
labels = [j for i in labels for j in i]
labels = [j for i in labels for j in i]
labels = [j for i in labels for j in i]

features['labels'] = labels
print(type(features['Latency'].values[0]))

features['Latency'] = features['Latency'].apply(lambda x: float(x)/125**2)

# see how it looks on feature space
sns.pairplot(features, hue='labels')
sns.catplot(data=features, x="labels", y="Latency", kind="box")
sns.catplot(data=features, x="labels", y="Amplitude", kind="box")

sns.jointplot(data=features, x="Latency", y="Amplitude",  hue='labels',  kind="kde")


