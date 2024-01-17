import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$&*%."
string=lower+upper+numbers+symbols
length=int(input("Please input the length of the password: "))
password="".join(random.sample(string,length))
print("Your new password is: "+password)