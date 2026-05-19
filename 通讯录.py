contact = {}

def add_contact():
    print('添加联系人')
    name = input('请输入联系人的姓名：')

    if not name:
        print('姓名不能为空')
        return
    if name in contact:
        print(f'{name}已存在，请移步修改功能')
        return
    
    contact[name] = {'phone': phone}
    print(f'{name}已添加')

def del_contact():
    print('删除联系人')
    name = input('请输入想要删除的名字')

    if not name:
        return
    if name not in contact:
        print(f'找不到{name}的联系人')
        return
    del contact[name]
    print(f'{name}已删除')

def search_contact():
    print('查找联系人')
    search_name = input('请输入想要查找的姓名')

    if not search_name:
        return 
    if search_name not in contact:
        print(f'找不到{search_name}的联系人')
        return
    
    print(f'姓名：{search_name},电话：{contact[search_name]}')  

def show_contact():
    print('显示联系人')
    if not contact:
        print('通讯录为空')
        return
    print(f'当前共有{len(contact)}位联系人')
    for name,info in contact.items():
        print(f'姓名：{name},电话：{info[phone]}')
    


while True:
    print('1.添加联系人')
    print('2.删除联系人')
    print('3.查找联系人')
    print('4.显示所有联系人')
    print('5.退出')
    choice = input('请输入你想要的操作：')
    if choice == '1':
        add_contact()
    elif choice == '2':
        del_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        show_contact()
    elif choice == '5':
        break
    else:
        print('输入无效')

    
    