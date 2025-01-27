while True:
    try:
        age = int(input("What is your age:: "))
        10/age
    except ValueError:
        print("Please enter a number:")
        continue
    except ZeroDivisionError:
        print(f"Please enter age higher than {age}")
        break
    else:
        print('Thank you')
        
    finally:
        print('Ok, I am finaly done!')
    print('Can you hear me: ')
    