import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
filename = ''  #フォルダのパスを入れる
df = pd.read_csv(filename, header=None, sep=',')

# 列名の設定
df.columns = ['time', 'battery_voltage', 'temperature', 
              'accel_x', 'accel_y', 'accel_z', 
              'gyro_x', 'gyro_y', 'gyro_z', 
              'mag_x', 'mag_y', 'mag_z']
plt.rcParams.update({'font.size': 30})  # ここで一括変更
# 1つのグラフを作成
plt.figure(figsize=(15, 10))
plt.scatter(df['time'], df['battery_voltage'], s=30, color='blue')
plt.title('Time vs Battery Voltage')
plt.xlabel('Time')
plt.ylabel('Battery Voltage [V]')
plt.grid()
plt.tight_layout()
plt.show()
