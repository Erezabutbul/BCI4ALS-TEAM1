

# Segmentation

markers = pd.read_csv(
    "https://raw.githubusercontent.com/Erezabutbul/BCI4ALS-TEAM1/62886db91df94f1799701c39e291b4a9d71d5ae3/src/output_files/Marker_Recordings/listOfMarkers_test.csv")

d = {'timeStamp': [], 'channel_1': [], 'channel_2': [], 'channel_3': [], 'channel_4': [], 'channel_5': [],
     'channel_6': [], 'channel_7': [], 'channel_8': [], 'channel_9': [], 'channel_10': [], 'channel_11': [],
     'channel_12': [], 'channel_13': [], 'channel_14': [], 'channel_15': [], 'channel_16': []}
baseline_df = pd.DataFrame(data=d)
distractor_df = pd.DataFrame(data=d)
target_df = pd.DataFrame(data=d)
baseline_N = 0
distractor_N = 0
target_N = 0
for i in markers['index'].values:
    if markers.iloc[i]['description'] == 'baseLine':
        boo = ((markers.iloc[i]['timeStamp']) < EEG_filtered['timeStamp']) & (
                    EEG_filtered['timeStamp'] < (markers.iloc[i]['timeStamp'] + window_size))
        start_ind = np.where(boo)[0][0]
        baseline_df_temp = EEG_filtered.iloc[int(start_ind) : (start_ind + window_size)]
        if baseline_df.empty:
            baseline_df = baseline_df_temp
        else:
            baseline_df['channel_1'] = baseline_df['channel_1'].values + baseline_df_temp['channel_1'].values
            baseline_df['channel_2'] = baseline_df['channel_2'].values + baseline_df_temp['channel_2'].values
            baseline_df['channel_3'] = baseline_df['channel_3'].values + baseline_df_temp['channel_3'].values
            baseline_df['channel_4'] = baseline_df['channel_4'].values + baseline_df_temp['channel_4'].values
            baseline_df['channel_5'] = baseline_df['channel_5'].values + baseline_df_temp['channel_5'].values
            baseline_df['channel_6'] = baseline_df['channel_6'].values + baseline_df_temp['channel_6'].values
            baseline_df['channel_7'] = baseline_df['channel_7'].values + baseline_df_temp['channel_7'].values
            baseline_df['channel_8'] = baseline_df['channel_8'].values + baseline_df_temp['channel_8'].values
            baseline_df['channel_9'] = baseline_df['channel_9'].values + baseline_df_temp['channel_9'].values
            baseline_df['channel_10'] = baseline_df['channel_10'].values + baseline_df_temp['channel_10'].values
            baseline_df['channel_11'] = baseline_df['channel_11'].values + baseline_df_temp['channel_11'].values
            baseline_df['channel_12'] = baseline_df['channel_12'].values + baseline_df_temp['channel_12'].values
            baseline_df['channel_13'] = baseline_df['channel_13'].values + baseline_df_temp['channel_13'].values
            baseline_df['channel_14'] = baseline_df['channel_14'].values + baseline_df_temp['channel_14'].values
            baseline_df['channel_15'] = baseline_df['channel_15'].values + baseline_df_temp['channel_15'].values
            baseline_df['channel_16'] = baseline_df['channel_16'].values + baseline_df_temp['channel_16'].values

            baseline_N = baseline_N + 1
    if markers.iloc[i]['description'] == 'distractor':
        boo = ((markers.iloc[i]['timeStamp']) < EEG_filtered['timeStamp']) & (
                    EEG_filtered['timeStamp'] < (markers.iloc[i]['timeStamp'] + window_size))
        start_ind = np.where(boo)[0][0]
        distractor_df_temp = EEG_filtered.iloc[int(start_ind) : (start_ind + window_size)]
        if distractor_df.empty:
            distractor_df = distractor_df_temp
        else:
            distractor_df['channel_1'] = distractor_df['channel_1'].values + distractor_df_temp['channel_1'].values
            distractor_df['channel_2'] = distractor_df['channel_2'].values + distractor_df_temp['channel_2'].values
            distractor_df['channel_3'] = distractor_df['channel_3'].values + distractor_df_temp['channel_3'].values
            distractor_df['channel_4'] = distractor_df['channel_4'].values + distractor_df_temp['channel_4'].values
            distractor_df['channel_5'] = distractor_df['channel_5'].values + distractor_df_temp['channel_5'].values
            distractor_df['channel_6'] = distractor_df['channel_6'].values + distractor_df_temp['channel_6'].values
            distractor_df['channel_7'] = distractor_df['channel_7'].values + distractor_df_temp['channel_7'].values
            distractor_df['channel_8'] = distractor_df['channel_8'].values + distractor_df_temp['channel_8'].values
            distractor_df['channel_9'] = distractor_df['channel_9'].values + distractor_df_temp['channel_9'].values
            distractor_df['channel_10'] = distractor_df['channel_10'].values + distractor_df_temp['channel_10'].values
            distractor_df['channel_11'] = distractor_df['channel_11'].values + distractor_df_temp['channel_11'].values
            distractor_df['channel_12'] = distractor_df['channel_12'].values + distractor_df_temp['channel_12'].values
            distractor_df['channel_13'] = distractor_df['channel_13'].values + distractor_df_temp['channel_13'].values
            distractor_df['channel_14'] = distractor_df['channel_14'].values + distractor_df_temp['channel_14'].values
            distractor_df['channel_15'] = distractor_df['channel_15'].values + distractor_df_temp['channel_15'].values
            distractor_df['channel_16'] = distractor_df['channel_16'].values + distractor_df_temp['channel_16'].values
            distractor_N = distractor_N + 1
    if markers.iloc[i]['description'] == 'target':
        boo = ((markers.iloc[i]['timeStamp']) < EEG_filtered['timeStamp']) & (
                EEG_filtered['timeStamp'] < (markers.iloc[i]['timeStamp'] + window_size))
        start_ind = np.where(boo)[0][0]
        target_df_temp = EEG_filtered.iloc[int(start_ind): (start_ind + window_size)]
        if target_df.empty:
            target_df = target_df_temp
        else:
            target_df['channel_1'] = target_df['channel_1'].values + target_df_temp['channel_1'].values
            target_df['channel_2'] = target_df['channel_2'].values + target_df_temp['channel_2'].values
            target_df['channel_3'] = target_df['channel_3'].values + target_df_temp['channel_3'].values
            target_df['channel_4'] = target_df['channel_4'].values + target_df_temp['channel_4'].values
            target_df['channel_5'] = target_df['channel_5'].values + target_df_temp['channel_5'].values
            target_df['channel_6'] = target_df['channel_6'].values + target_df_temp['channel_6'].values
            target_df['channel_7'] = target_df['channel_7'].values + target_df_temp['channel_7'].values
            target_df['channel_8'] = target_df['channel_8'].values + target_df_temp['channel_8'].values
            target_df['channel_9'] = target_df['channel_9'].values + target_df_temp['channel_9'].values
            target_df['channel_10'] = target_df['channel_10'].values + target_df_temp['channel_10'].values
            target_df['channel_11'] = target_df['channel_11'].values + target_df_temp['channel_11'].values
            target_df['channel_12'] = target_df['channel_12'].values + target_df_temp['channel_12'].values
            target_df['channel_13'] = target_df['channel_13'].values + target_df_temp['channel_13'].values
            target_df['channel_14'] = target_df['channel_14'].values + target_df_temp['channel_14'].values
            target_df['channel_15'] = target_df['channel_15'].values + target_df_temp['channel_15'].values
            target_df['channel_16'] = target_df['channel_16'].values + target_df_temp['channel_16'].values
            target_N = target_N + 1

# Dividing by the number of trails

            baseline_df['channel_1'] = baseline_df['channel_1'].values/baseline_N
            baseline_df['channel_2'] = baseline_df['channel_2'].values/baseline_N
            baseline_df['channel_3'] = baseline_df['channel_3'].values/baseline_N
            baseline_df['channel_4'] = baseline_df['channel_4'].values/baseline_N
            baseline_df['channel_5'] = baseline_df['channel_5'].values/baseline_N
            baseline_df['channel_6'] = baseline_df['channel_6'].values/baseline_N
            baseline_df['channel_7'] = baseline_df['channel_7'].values/baseline_N
            baseline_df['channel_8'] = baseline_df['channel_8'].values/baseline_N
            baseline_df['channel_9'] = baseline_df['channel_9'].values/baseline_N
            baseline_df['channel_10'] = baseline_df['channel_10'].values/baseline_N
            baseline_df['channel_11'] = baseline_df['channel_11'].values/baseline_N
            baseline_df['channel_12'] = baseline_df['channel_12'].values/baseline_N
            baseline_df['channel_13'] = baseline_df['channel_13'].values/baseline_N
            baseline_df['channel_14'] = baseline_df['channel_14'].values/baseline_N
            baseline_df['channel_15'] = baseline_df['channel_15'].values/baseline_N
            baseline_df['channel_16'] = baseline_df['channel_16'].values/baseline_N

            distractor_df['channel_1'] = distractor_df['channel_1'].values/distractor_N
            distractor_df['channel_2'] = distractor_df['channel_2'].values/distractor_N
            distractor_df['channel_3'] = distractor_df['channel_3'].values/distractor_N
            distractor_df['channel_4'] = distractor_df['channel_4'].values/distractor_N
            distractor_df['channel_5'] = distractor_df['channel_5'].values/distractor_N
            distractor_df['channel_6'] = distractor_df['channel_6'].values/distractor_N
            distractor_df['channel_7'] = distractor_df['channel_7'].values/distractor_N
            distractor_df['channel_8'] = distractor_df['channel_8'].values/distractor_N
            distractor_df['channel_9'] = distractor_df['channel_9'].values/distractor_N
            distractor_df['channel_10'] = distractor_df['channel_10'].values/distractor_N
            distractor_df['channel_11'] = distractor_df['channel_11'].values/distractor_N
            distractor_df['channel_12'] = distractor_df['channel_12'].values/distractor_N
            distractor_df['channel_13'] = distractor_df['channel_13'].values/distractor_N
            distractor_df['channel_14'] = distractor_df['channel_14'].values/distractor_N
            distractor_df['channel_15'] = distractor_df['channel_15'].values/distractor_N
            distractor_df['channel_16'] = distractor_df['channel_16'].values/distractor_N

            target_df['channel_1'] = target_df['channel_1'].values/target_N
            target_df['channel_2'] = target_df['channel_2'].values/target_N
            target_df['channel_3'] = target_df['channel_3'].values/target_N
            target_df['channel_4'] = target_df['channel_4'].values/target_N
            target_df['channel_5'] = target_df['channel_5'].values/target_N
            target_df['channel_6'] = target_df['channel_6'].values/target_N
            target_df['channel_7'] = target_df['channel_7'].values/target_N
            target_df['channel_8'] = target_df['channel_8'].values/target_N
            target_df['channel_9'] = target_df['channel_9'].values/target_N
            target_df['channel_10'] = target_df['channel_10'].values/target_N
            target_df['channel_11'] = target_df['channel_11'].values/target_N
            target_df['channel_12'] = target_df['channel_12'].values/target_N
            target_df['channel_13'] = target_df['channel_13'].values/target_N
            target_df['channel_14'] = target_df['channel_14'].values/target_N
            target_df['channel_15'] = target_df['channel_15'].values/target_N
            target_df['channel_16'] = target_df['channel_16'].values/target_N



# ERP Visualization

fig5, ax5 = plt.subplots()

ax5.plot(baseline_df['channel_1'].values, label='Electrode 1')
ax5.plot(baseline_df['channel_2'].values, label='Electrode 2')
ax5.plot(baseline_df['channel_3'].values, label='Electrode 3')
ax5.plot(baseline_df['channel_4'].values, label='Electrode 4')
ax5.plot(baseline_df['channel_5'].values, label='Electrode 5')
ax5.plot(baseline_df['channel_6'].values, label='Electrode 6')
ax5.plot(baseline_df['channel_7'].values, label='Electrode 7')
ax5.plot(baseline_df['channel_8'].values, label='Electrode 8')
ax5.plot(baseline_df['channel_9'].values, label='Electrode 9')
ax5.plot(baseline_df['channel_10'].values, label='Electrode 10')
ax5.plot(baseline_df['channel_11'].values, label='Electrode 11')
ax5.plot(baseline_df['channel_12'].values, label='Electrode 12')
ax5.plot(baseline_df['channel_13'].values, label='Electrode 13')
ax5.plot(baseline_df['channel_14'].values, label='Electrode 14')
ax5.plot(baseline_df['channel_15'].values, label='Electrode 15')
ax5.plot(baseline_df['channel_16'].values, label='Electrode 16')

ax5.legend()
ax5.set(xlabel='Time [Seconds]', ylabel='Voltage [mV]')

fig5.suptitle("""ERP baseline Per Electrode\n\n""", fontweight="bold")


fig6, ax6 = plt.subplots()

ax6.plot(distractor_df['channel_1'].values, label='Electrode 1')
ax6.plot(distractor_df['channel_2'].values, label='Electrode 2')
ax6.plot(distractor_df['channel_3'].values, label='Electrode 3')
ax6.plot(distractor_df['channel_4'].values, label='Electrode 4')
ax6.plot(distractor_df['channel_5'].values, label='Electrode 5')
ax6.plot(distractor_df['channel_6'].values, label='Electrode 6')
ax6.plot(distractor_df['channel_7'].values, label='Electrode 7')
ax6.plot(distractor_df['channel_8'].values, label='Electrode 8')
ax6.plot(distractor_df['channel_9'].values, label='Electrode 9')
ax6.plot(distractor_df['channel_10'].values, label='Electrode 10')
ax6.plot(distractor_df['channel_11'].values, label='Electrode 11')
ax6.plot(distractor_df['channel_12'].values, label='Electrode 12')
ax6.plot(distractor_df['channel_13'].values, label='Electrode 13')
ax6.plot(distractor_df['channel_14'].values, label='Electrode 14')
ax6.plot(distractor_df['channel_15'].values, label='Electrode 15')
ax6.plot(distractor_df['channel_16'].values, label='Electrode 16')

ax6.legend()
ax6.set(xlabel='Time [Seconds]', ylabel='Voltage [mV]')
fig6.suptitle("""ERP Distractor Per Electrode\n\n""", fontweight="bold")

fig7, ax7 = plt.subplots()

ax7.plot(target_df['channel_1'].values, label='Electrode 1')
ax7.plot(target_df['channel_2'].values, label='Electrode 2')
ax7.plot(target_df['channel_3'].values, label='Electrode 3')
ax7.plot(target_df['channel_4'].values, label='Electrode 4')
ax7.plot(target_df['channel_5'].values, label='Electrode 5')
ax7.plot(target_df['channel_6'].values, label='Electrode 6')
ax7.plot(target_df['channel_7'].values, label='Electrode 7')
ax7.plot(target_df['channel_8'].values, label='Electrode 8')
ax7.plot(target_df['channel_9'].values, label='Electrode 9')
ax7.plot(target_df['channel_10'].values, label='Electrode 10')
ax7.plot(target_df['channel_11'].values, label='Electrode 11')
ax7.plot(target_df['channel_12'].values, label='Electrode 12')
ax7.plot(target_df['channel_13'].values, label='Electrode 13')
ax7.plot(target_df['channel_14'].values, label='Electrode 14')
ax7.plot(target_df['channel_15'].values, label='Electrode 15')
ax7.plot(target_df['channel_16'].values, label='Electrode 16')

ax7.legend()
ax7.set(xlabel='Time [Seconds]', ylabel='Voltage [mV]')
fig7.suptitle("""ERP Target Per Electrode\n\n""", fontweight="bold")

plt.show()


print(d)
# baseline
