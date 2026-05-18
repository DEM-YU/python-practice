answer = 66

while True:
    num = int(input('请猜测这个数字是多少：'))
    if num == answer:
        print('right')
        break
    elif num > answer:
        print('Too big')
    else:
        print('Too small')


