'''
Pasword checker programmer
'''

userName = input('Enter User Name: ')
password_value= input('Enter Password: ')
pass_len =  len(password_value)
hiddenPass = '*' * pass_len
print(f'User Name = {userName} & Password = { hiddenPass} and length of password is :: {pass_len}')


