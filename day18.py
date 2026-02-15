#read
#write
#append


# f=open('day17.py',"r")
# print(f.read())


# f=open("data.txt",'w')
# f.write("update this file 2 ")
# f.close()


# f=open("data2.txt",'a')         #ADD at last
# f.write("update this file 3")
# f.close()


# f=open("data2.txt",'r+')
# f.write("ddddd")
# f.close()


# f=open("data3.txt",'w+')
# f.write("whats up")
# f.close()



# try:
#      b=10
#      print(d)
    
# except:
#     print("something went wrong")
    
    
    
    
# try:
#     b=10
#     print(b/0)
    
# except TypeError as e:
#     print(e)
    
# except NameError as e:
#     print(e)
    
# except:
#     print("something went wrong")
    
    
    

    
    
from datetime import datetime
time=datetime.now()
def handle_error(file_name, error):
    f = open("file_name", "a")
    f.write(f'\n {time} {error}')
    f.close()
    return


b = 50
try:
    b = b / 0
except ZeroDivisionError as e:
    handle_error("zero.txt", str(e))
except NameError as e:
    handle_error("name.txt", str(e))

except:
    handle_error("error.txt", str(e))

