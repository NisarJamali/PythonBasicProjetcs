from cryptography.fernet import Fernet

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close
    return key




master_pwm = input("Enter master password: ")

key = load_key() + master_pwm.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rsplit(), fer.decrypt(line.encode()))
            
            
def add():
    name = input('Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode + '\n')

while True :
    mode = input('Do you want to add new password or view existing one (add/view) or Q to quit: ').lower()
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else :
        print("Invalid mode.")
        continue
