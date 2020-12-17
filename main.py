import re 

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
      
def check_email(email):  
    if(re.search(regex,email)):  
        return True          
    else:  
        return False 
      
def check_psw_upper(psw):
  result = any(char.isupper() for char in psw)
  return result

def check_psw_digit(psw):
  result = any(char.isdigit() for char in psw)
  return result

#Maybe set an not before to make it wrong?
def check_psw_lower(psw):
  result = not any(char.islower() for char in psw)
  return result

def check_psw(psw):
  if(check_psw_digit(psw)
            and check_psw_upper(psw)
            and check_psw_lower(psw)
            and len(psw) > 7):
    print("Valid password")
    return True
  else:
    print("Invalid password")    
    return False    






