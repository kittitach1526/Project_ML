import pandas as pd


# อ่านไฟล์ CSV
df = pd.read_csv('csv/full_Data/blue/blue_1.csv')

# print(df)

# กรองข้อมูลเพื่อไม่เอา 10 วินาทีแรกและ 10 วินาทีหลัง
start_time = df['Time (s)'].min() + 10
end_time = df['Time (s)'].max() - 10
filtered_df = df[(df['Time (s)'] > start_time) & (df['Time (s)'] < end_time)]

# แสดงข้อมูลทั้งหมดใน DataFrame หาค่าเฉลี่ยของ Gyroscope x (rad/s)
print(filtered_df['Gyroscope x (rad/s)'])
mean_gyro_x = filtered_df['Gyroscope x (rad/s)'].mean()
print(f"ค่าเฉลี่ยของ Gyroscope x (rad/s): {mean_gyro_x}")

# หาค่ามากสุดและน้อยสุดของคอลัมน์ 'Gyroscope x (rad/s)'
max_gyro_x = filtered_df['Gyroscope x (rad/s)'].max()
min_gyro_x = filtered_df['Gyroscope x (rad/s)'].min()
print(f"ค่ามากสุดของ Gyroscope x (rad/s): {max_gyro_x}")
print(f"ค่าน้อยสุดของ Gyroscope x (rad/s): {min_gyro_x}")

# คำนวณขอบเขตของค่าเฉลี่ย +- 1.5
lower_bound = mean_gyro_x - 0.15
upper_bound = mean_gyro_x + 0.15
filtered_extreme_values = filtered_df[(filtered_df['Gyroscope x (rad/s)'] < lower_bound) | (filtered_df['Gyroscope x (rad/s)'] > upper_bound)]

print(filtered_extreme_values)

# บันทึกข้อมูลที่กรองแล้วลงในไฟล์
with open('filtered_data.txt', 'a') as file:
    # ตรวจสอบว่าไฟล์ว่างหรือไม่ ถ้าว่างให้เขียน header
    if file.tell() == 0:
        file.write("id,label,time,gyro_x,gyro_y,gyro_z;\n")  # ปรับให้ตรงกับคอลัมน์ในไฟล์

    # วนดูข้อมูลในแต่ละแถวและเขียนลงไฟล์
    for index, row in filtered_extreme_values.iterrows():
        # เขียนข้อมูลของแต่ละแถวลงในไฟล์ตามรูปแบบที่กำหนด
        file.write(f"11,turn,{row['Time (s)']},{row['Gyroscope x (rad/s)']},{row['Gyroscope y (rad/s)']},{row['Gyroscope z (rad/s)']};\n")
