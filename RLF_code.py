# Function to get user data
def fetch():
  db = open("database.txt", "r")
  user_exist = input("Enter your username: ")
  pass_exist = input("Enter your password: ")

  # Checking whether an input has been given or not
  if not len(user_exist or pass_exist) < 1:
    users = []
    passwords = []

    # Looping to get dictionary of all the lines from our text file
    for i in db:
      a,b = i.split(", ")
      b = b.strip()
      users.append(a)
      passwords.append(b)

    data = dict(zip(users, passwords))

    # Data validation to make sure information is present
    try:
      if data[user_exist]:
        try:
          if pass_exist == data[user_exist]:
            print("Login successful!")
            print("Hello,", user_exist)
          else:
            print("Password or username incorrect! Try again.")
            fetch()
        except:
          print("Incorrect password or username!")
      else:
        print("USername does not exist. Please check username or register!")
        choose()
    except:
      print("Login error! Check your information or register.")
      choose()
  else:
    print("Please enter something.")

# Function to register a user
def registration():
  db = open("database.txt", "r")
  user = input("Enter/create a username: ")
  email = input("Enter your email: ")

  # Email validation function call
  valid_email(email)

  print("NOTE: Password must contain one digit, one lowercase character, one uppercase character and one special")  
  passwrd = input("Enter/create a password: ")

  # PAssword validation function call
  valid_password(passwrd)
  conf_passwrd = input("Confirm your password: ")
  # users = []
  # passwords = []

  # for i in db:
  #   a,b = i.split(", ")
  #   b = b.strip()
  #   users.append(a)
  #   passwords.append(b)
  
  # info = dict(zip(users, passwords))
  # # print(info)

  # Basic password validation during registration
  if passwrd != conf_passwrd:
    print("Passwords don't match, please restart!")
    registration()
  elif len(passwrd)<5 or len(passwrd)>16:
    print("Password length is too short or too long, start again!")
  elif user in users:
    print("Username already exists, choose a different one.")
    registration()
  else:
    db = open("database.txt", "a")
    db.write(user+ ", " +passwrd+ "\n")
    print("Registration successful!")

# Function to fetch password for registered user
def get_pass():
  # print(info)
  db = open("database.txt", "r")
  user = input("To fetch your forgoteen password, please enter your username: ")
  users = []
  passwords = []
  for i in db:
    a,b = i.split(", ")
    b = b.strip()
    users.append(a)
    passwords.append(b)
  
  info = dict(zip(users, passwords))
  # print(info.get(user))
  if user in info:
    print("Here's your password: ", info.get(user))
    print("NOTE: Do not share your password with anyone.")
  else:
    print("User does not exist")
    print("You might want to register.")
    choose()

# Function for email validation
def valid_email(email):
  if '@' not in email:
     print("Please enter a valid email")
     email = input("Enter your email: ")
  ind = email.index("@")
  if ".com" not in email[ind:] or "@." in email:
     print("Please enter a valid email")
     email = input("Enter your email: ")
     valid_email(email)

# Function for password validation
def valid_password(pword):
  symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
  val = True

  if len(pword) < 5:
    print('Length should be at least 5 characters long')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
        
  elif len(pword) > 16:
    print('Length should be not be greater than 16 characters')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
          
  elif not any(char.isdigit() for char in pword):
    print('Password should at least have one digit')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
          
  elif not any(char.isupper() for char in pword):
    print('Password should at least have one uppercase letter')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
          
  elif not any(char.islower() for char in pword):
    print('Password should at least have one lowercase letter')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
          
  elif not any(char in symbols for char in pword):
    print('Password should at least have one special character')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)
  
  elif pword[0] in symbols:
    print('Password cannot begin with a special character')
    val = False
    passwrd = input("Enter/create a password: ")
    valid_password(passwrd)

  elif val:
    return val

# Main function
def choose(option=None):
  print('Choose an option: ')
  print('''
  1. Login
  2. Register
  3. Forgot Password''')
  option = input()
  if option == "1":
    fetch()
  elif option == "2":
    registration()
  elif option == "3":
    get_pass()
  else:
    print("Please select an option.")
    choose()

choose()
