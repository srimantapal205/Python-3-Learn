# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Sorna2',
    'valid': False 
}

def authenticated(fn):
  # code here
  def WrapperFunction(*args, **kwargs):
    if args[0]["valid"]:
          return fn(*args, **kwargs)
    else:
        print('Invalid user..... :(')
  return WrapperFunction  

@authenticated
def message_friends(user):
    print(f'{user['name']} :: message has been sent')
    
message_friends(user1)
message_friends(user2)