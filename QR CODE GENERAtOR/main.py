import qrcode

url=input("Enter the url of the web page: ")

file_Name=input("Enter the name u want to save it: ")

if not(file_Name.endswith(".png")): 
    file_Name= file_Name + ".png"

img = qrcode.make(url)
img.save(file_Name)



