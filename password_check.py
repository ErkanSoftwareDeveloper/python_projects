def password_check():
  password = 78312
  input_password = int(input("Write your password, to enter: "))

  if password == input_password:
    print("Correct! you can join")
  else:
    print("Its Wrong")
if __name__=="__main__":
  password_check()
