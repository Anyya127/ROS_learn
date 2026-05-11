print("温度转化器")
print("输入温度值，后面跟上单位（C或F），例如：36.6C 或 97.88F")
temp_input = input("请输入温度值：")
if temp_input[-1].upper() == 'C':
    celsius = float(temp_input[:-1])
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C 转换为 {fahrenheit:.2f}°F")
elif temp_input[-1].upper() == 'F':
    fahrenheit = float(temp_input[:-1])
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F 转换为 {celsius:.2f}°C")
else:
    print("输入格式错误，请确保温度值后面跟上单位（C或F）。")
    