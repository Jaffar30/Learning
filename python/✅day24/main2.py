# file_you_want_to_open , mode
# .read() : return file content as a string
# .close() : close the file , to free up system resources
file = open(r'C:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day24\my_file.txt')
contents = file.read()
print(contents)
file.close()