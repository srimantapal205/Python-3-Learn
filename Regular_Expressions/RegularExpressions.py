import re
text = "Contact us at support@example.com or sales@mywebsite.org"

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)


# Password Checker

passwordPattrn = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"

password = 'P@ssw0rdA@2'
password2 = 'Password'
password3 = 'Passwor'

def passwordChecker(item):
    checkPass = re.fullmatch(passwordPattrn, item)
    if checkPass:
        print("Password Pattern is matched :)")
    elif 8>len(item)<16:
        print("Password minimum lenth is 8 :(")
    else:
        print("Password Pattern is not matched :(")
        
passwordChecker(password)
passwordChecker(password2)
passwordChecker(password3)

