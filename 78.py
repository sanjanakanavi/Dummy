# file handling in python
'main methods are :open ,close ,read ,write'
"""open file syntax:
fileobject=open("filename","mode")
fileobject:it points towards the location of file in permanent memory
mode :in which mode a should open
six types of modes are there:
  read , write , append(add something at the end) , read+ , write+ , append+"""

# once u create a file and then try to execute same again then u cant create bcz same name files cant be created
# f1 = open("file_1", "x")  #x mode is to just create empty file'

'if u dont mention r also then by default its r only,raises i/o error if file doesnot exists'
# r will open file in read mode and pointer is at the begining of the file
# f1 = open("file_1", "r")
# data = f1.read()  # function to fetch the data from file
# print(data)

"""w:write mode: opens the file in write mode only,it overwrites the file if file already exists or 
it will create a new file if file doesnot exist,the file handler exists at the begining"""
# f1 = open("file_1", "w")
# f1.write("hi im in dharwad")  # writing content in file

'again opening file in read mode then reading the file'
# f1 = open("file_1", "r")
# print(f1.read())  # reading the file

'r+ mode:opens file in both read and write mode,filehandler already exists at the begining'
'raises i/o error if file doesnot exists'
'this is used when u want to read first then write in file,previous data will be present'
# f1 = open("file_1", "r+")
# print(f1.read())  # reading
# f1.write("hi im in python class")  # writing
'if above statements interchanged like shown below,then data will be rewritten or modified from starting point'
'file will be read from where the cursor is present'
# f1 = open("file_1", "r+")
# f1.write("hi")  # writing
# print(f1.read())  # reading
# print(f1.tell())  # this function will give position of cursor

'w+ mode:opens file in both read and write mode,filehandler already exists at the begining'
'it overwrites the previous content of the opened file if the file already exists,if not it creates new file'
# f1 = open("file_1", "w+")
# f1.write("hi welcome to python")
# print(f1.tell())
# f1.seek(0)  # seek function moves cursor whichever position we want
# print(f1.read())  # here it will print ntg bcz cursor is at the end

'''a:append mode: opens the file in append or write mode.the file handler exists at the end of the previously written file
if file already exists. if file doesnt exists it creates a new file,the newly written data will be added at the end of the file'''
'here u cant read the file'
# f1 = open("file_1", "a")
# f1.write(" jai shree ram")#adds data at the end

'''a+:append+ mode: it is same as append a mode but we can read the file here'''
# f1 = open("file_1", "a+")
# f1.write(" jai shree krishna")
# f1.seek(0)
# print(f1.read())

'''if we want to do operations on file present on desktop then u have to put complete link
of that file in place of filename ,example in below'''
# f1=open("C:\Users\sanja\OneDrive\Desktop\jkhgg.txt","a+")
# f1.write("hi im sanjana")

'''if you want to operate on pic ,then u should put image file name.jpg in place of filename and 
for everymode u should attach b like 'rb' to access image/binary files'''
'example below'
# f1 = open("pic1.jpg", "rb")
# print(f1.read())
# f2 = open("pic2.jpg", "wb+")  # write mode
# for i in f1:
# putting image from f1 to f2 using for loop,this creates new jpg file
#    f2.write(i)
# print(f2.read())

'method to read image'
# import io
# from PIL import Image
'''
# Open the image file in binary mode
with open("pic1.jpg", "rb") as f1:
    # Read the binary content of the image
    img_data = f1.read()

# Create a BytesIO object to wrap the binary data
img_stream = io.BytesIO(img_data)

# Open the image using Pillow
image = Image.open(img_stream)

# Display the image
image.show()
'''
