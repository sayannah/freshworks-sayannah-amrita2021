#here are the commands to demonstrate how to access and perform operations on a main file
import time

#run the MODULE of MAIN FILE and import mainfile as a library
import threading

import code as x
#importing the main file("code" is the name of the file I have used) as a library
x.d={}
print(x.d)
x.create("sayannah",25,10)
#to create a key with key_name,value given and with no time-to-live property


x.create("src",70,3600)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("sayannah")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("sayannah",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("sayannah",55)
#it replaces the initial value of the respective key with new value



x.delete("sayannah")
# x.delete("src")
#it deletes the respective key and its value from the database(memory is also freed)
key_name="sayannah"
value=55
timeout=10
#we can access these using multiple threads like
t1=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
time.sleep(0.2)
t2=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
time.sleep(0.2)
#and so on upto tn
print(x.d)
#the code also returns other errors like
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

