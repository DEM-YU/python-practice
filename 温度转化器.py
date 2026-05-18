print('华氏度转换摄氏度 输入1，摄氏度转换华氏度请输入2')
try:
    num = int(input('输入你的选择：'))
    if num == 1:
        tem = int(input('请输入华氏度：'))
        F = (tem - 32) * 5/9
        print(F)
    elif num == 2:
        tem = int(input('请输入摄氏度：'))
    C = tem * 9/5 + 32
    print(C)    
except ValueError:
    print("Invalid input")

