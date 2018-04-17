#Alinea Grace Del Mundo
#File Handling

text_file = open("text.txt",'w')
text_file.write("Hi ! Welcome to  !")
text_file.close()
text_file = open("text.txt",'a')
text_file.write(" My life")
text_file.close()


# to display in run!
# text_file = open("text.txt",'r')
# print(text_file.read())
# text_file.close()
