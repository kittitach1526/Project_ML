import xlrd
import csv

def xls_to_csv(xls_file, csv_file):
    # เปิดไฟล์ .xls
    workbook = xlrd.open_workbook(xls_file)
    sheet = workbook.sheet_by_index(0)  # ใช้ Sheet แรก

    # เปิดไฟล์ .csv สำหรับเขียนข้อมูล
    with open(csv_file, mode="w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        # อ่านข้อมูลจาก .xls แล้วเขียนลง .csv
        for row_idx in range(sheet.nrows):
            row_data = sheet.row_values(row_idx)  # ดึงข้อมูลแต่ละแถว
            csv_writer.writerow(row_data)

    print(f"ไฟล์ {xls_file} ถูกแปลงเป็น {csv_file} สำเร็จแล้ว!")

# ตัวอย่างการเรียกใช้
xls_file_path = "record/blue/3.xls"  # ระบุ path ของไฟล์ .xls
csv_file_path = "blue_3.csv"  # ระบุ path ที่ต้องการบันทึกไฟล์ .csv

xls_to_csv(xls_file_path, csv_file_path)
