f1=r'C:\Users\Dell lap\Desktop\index.png'
f2=r'D:\training\Python\oracle\may1\new.png'

fh_1 = open(f1, 'rb')
fh_2 = open(f2, 'wb')
fh_2.write(fh_1.read())

fh_1.close()
fh_2.close()