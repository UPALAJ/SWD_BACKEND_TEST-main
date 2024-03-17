
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def num_to_thai_text(number):
    if number == 0:
        return "ศูนย์"
    
    units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    tens = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
    text = ""
    str_num = str(number)
    
    for i in range(len(str_num)):
        n = int(str_num[i])
        position = len(str_num) - i - 1
        if n > 0:
            if position == 0 and n == 1 and len(str_num) > 1:
                text += "เอ็ด"
            elif position == 1 and n == 2:
                text += "ยี่สิบ"
            elif position == 1 and n == 1:
                text += "สิบ"
            else:
                text += units[n] + tens[position]
        elif n == 0 and position == 6:
            text += tens[position]
    
    return text

