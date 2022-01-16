import os
os.system('cmd /k "chcp 1256"')
import easyocr

reader = easyocr.Reader(["ar","fa","ur","ug","en"])
result = reader.readtext('C:/Users/ASUS/arabic.jpg')
print(result)