
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def arabic_to_roman(number):
    result = ""
    
    roman_numbers = {
        1: "I", 
        4: "IV", 
        5: "V", 
        9: "IX",
        10: "X", 
        40: "XL", 
        50: "L", 
        90: "XC",
        100: "C", 
        400: "CD", 
        500: "D", 
        900: "CM",
        1000: "M"
    }
    
    
    for value in sorted(roman_numbers.keys(), reverse=True):
        while number >= value:
            result += roman_numbers[value]
            number -= value
    
    return result
