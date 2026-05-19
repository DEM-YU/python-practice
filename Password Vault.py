password_book = {}

def add_password():
    print('add your password')
    website = input('which website do you want to add?')
    
    if not website:
        return
    if website in password_book:
        return
    password = input('what is the password for this website?')
    if not password:
        return
    account = input('which account you used for this website?')
    if not account:
        return 

    password_book[website] = {'account':account, 'password':password}
    print(f'{website} add successfully')

def del_password():
    print('del your password')
    website = input('choose which website to del:')

    if website not in password_book:
        return
    
    del password_book[website]
    print(f"{website}'s password had already deleted")

def search_password():
    print('search the password')
    website = input('which website do you want to search:')

    if not website:
        return 
    if website not in password_book:
        return 
    print(f'website: {website}, account: {password_book[website]["account"]}, password: {password_book[website]["password"]}')
def change_password():
    print('change the password')
    website = input('which website do you want to change:')

    if not website:
        return
    if website not in password_book:
        return
    new_password = input('what is the new password for this website?')
    if not new_password:
        return
    password_book[website]['password'] = new_password
    print(f'{website} change password successfully')    

def show_password():
    print('show all password')
    if not password_book:
        return
    for website, info in password_book.items():
        print(f'website: {website}, account: {info["account"]}, password: {info["password"]}')

while True:
    print('1.add password')
    print('2.del password')
    print('3.search password')
    print('4.change password')
    print('5.show all password')
    print('6.exit')
    choice = input('choose which operation you want to do:')
    if choice == '1':
        add_password()
    elif choice == '2':
        del_password()
    elif choice == '3':
        search_password()
    elif choice == '4':
        change_password()
    elif choice == '5':
        show_password()
    elif choice == '6': 
        break
    else:
        print('invalid input')


