
import pytest
from main import check_psw
from main import check_email
        
def test_email1():
  email = "ankitrai326@gmail.com"
  assert check_email(email) is True

def test_email2():
  email = "my.ownsite@ourearth.org"
  assert check_email(email) is True

def test_email3():
  email = "ankitrai326.com"
  assert check_email(email) is False

def test_check_psw1():
  psw = "Hejhej1234"
  assert check_psw(psw) is True

def test_check_psw2():
  psw = "hejhej"
  assert check_psw(psw) is False

def test_check_psw3():
  psw = "HEJHEJ55"
  assert check_psw(psw) is False
  
def test_check_psw4():
  psw = "Hejhej"
  assert check_psw(psw) is False
  
def test_check_psw5():
  psw = "551234"
  assert check_psw(psw) is False

def test_check_psw6():
  psw = "Hejhej$£@55"
  assert check_psw(psw) is True

def test_check_psw7():
  psw = "Hejhej$£@"
  assert check_psw(psw) is False
     
  

