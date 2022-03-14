import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name_07 = 'E:/Python/Data_Download/sitka_weather_07-2018_simple.csv'
file_name_full = 'E:/Python/Data_Download/sitka_weather_2018_simple.csv'
with open(file_name_full) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 从文件中获取日期信息

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],  '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)

    plt.style.use('bmh')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='darkorange', alpha=0.5)
    ax.plot(dates, lows, c='violet', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='lightgray', alpha=1)
    ax.set_title('The maximum and minimum of temperature of everyday in 2018')
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('temperature', fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

    first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
    print(first_date)