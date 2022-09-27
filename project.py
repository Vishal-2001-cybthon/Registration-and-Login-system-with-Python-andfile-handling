import os
!pip install email_validator
!pip install password-validator

from email_validator import validate_email,EmailNotValidError
from password_validator import PasswordValidator

def Login():
  E_mail_id=input("Enter your registered E_mail-id: ")
  try:
   validation=validate_email(E_mail_id,check_deliverability=False)
   email=validation.email
  except EmailNotValidError as e:
    print(str(e))
  Pwd=input("Enter your registered Pwd: ")
  schema=PasswordValidator()
  schema\
  .min(8)\
  .max(100)\
  .has().uppercase()\
  .has().lowercase()\
  .has().digits()\
  .has().symbols()\
  
  schema.validate(Pwd)
  txt_file=open("visabi.txt","r+")
  reader=txt_file.read()
  if E_mail_id and Pwd in reader:
    print("Login Sucessfull""\n" "Welcome to GUVI Dashboard!!!")
    welcome()
  else:
    print("mailid and pwd not valid")
    Login()

def welcome():
  print("Hii All\nChoose an option:")
  option=input("Login|Signup :")
  if option=="login" or option=="Login":
    Login()
  elif option=="signup" or option=="Signup":
    Sign_up()
  else:
    print("choose the crct option")
    welcome()
welcome()

def Sign_up():
  Email_id=input("Enter the Mail_id: ")
  try:
   validation=validate_email(Email_id,check_deliverability=True)
   email=validation.email
  except EmailNotValidError as e:
    print(str(e))
    Sign_up()
  
  Pass_word=input("Enter the Password: ") 
  schema=PasswordValidator()
  schema\
  .min(8)\
  .max(100)\
  .has().uppercase()\
  .has().lowercase()\
  .has().digits()\
  .has().symbols()\
  
  schema.validate(Pass_word)
  txt_file=open("visabi.txt","r+")
  reader_1=txt_file.read()
  if Email_id and Pass_word in reader_1:
    print("regitered email and pwd exists")
    Login()
  else:
    txt_file=open("visabi.txt","a")
    txt_file.write(" ,"+Email_id+", "+Pass_word)
    txt_file.close()
    print("registration sucessful")
    Login()
Sign_up()
