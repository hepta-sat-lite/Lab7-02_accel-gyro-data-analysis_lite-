import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
filename = '/content/test.txt'  # 実際のファイル名に合わせる
df = pd.read_csv(filename, header=None, sep=',')

# 列名の設定
df.columns = ['time', 'battery_voltage', 'temperature', 
              'accel_x', 'accel_y', 'accel_z', 
              'gyro_x', 'gyro_y', 'gyro_z', 
              'mag_x', 'mag_y', 'mag_z']

# 数値に変換できない列の変換（必要に応じて）
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df['accel_y'] = pd.to_numeric(df['accel_y'], errors='coerce')
df['gyro_x'] = pd.to_numeric(df['gyro_x'], errors='coerce')

# プロット作成（ドットプロット）
plt.figure(figsize=(15, 10))

# 1. 時間 - バッテリー電圧
plt.subplot(4, 1, 1)
plt.scatter(df['time'], df['battery_voltage'], s=10)
plt.title('Battery Voltage vs Time')
plt.xlabel('Time')
plt.ylabel('Battery Voltage (V)')
plt.grid()

# 2. 時間 - 温度（サブプロットの行数を4に統一）
plt.subplot(4, 1, 2)
plt.scatter(df['time'], df['temperature'], s=10)
plt.title('Temperature vs Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.grid()

# 3. 時間 - 加速度(x, y, z)
plt.subplot(4, 1, 3)
plt.scatter(df['time'], df['accel_x'], s=10, label='Accel X')
plt.scatter(df['time'], df['accel_y'], s=10, label='Accel Y')
plt.scatter(df['time'], df['accel_z'], s=10, label='Accel Z')
plt.title('Acceleration (X, Y, Z) vs Time')
plt.xlabel('Time')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.grid()

# 4. 時間 - 角速度(x, y, z)
plt.subplot(4, 1, 4)
plt.scatter(df['time'], df['gyro_x'], s=10, label='Gyro X')
plt.scatter(df['time'], df['gyro_y'], s=10, label='Gyro Y')
plt.scatter(df['time'], df['gyro_z'], s=10, label='Gyro Z')
plt.title('Gyro (X, Y, Z) vs Time')
plt.xlabel('Time')
plt.ylabel('Gyro (deg/s)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
