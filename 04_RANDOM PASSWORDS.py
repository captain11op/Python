import random as r 


keys = ("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")
passlen = int(input("How much letters u want the password should be:"))
password = ""



for i in range(passlen):
 z = r.choice(keys)
 password +=  z
     
print(password)


     
     