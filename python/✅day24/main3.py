# file_you_want_to_open , mode
# .read() : return file content as a string
# .close() : close the file , to free up system resources

# differant way to open and close file using with statement
# dont have the need to explicitly close the file its automatically closed

# with open(r'C:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day24\my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# write to the file
# a = append mode (adds content to the end of the file)
# w = write mode (overwrites existing content)
# r or empty = read mode
with open(r'C:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day24\my_file.txt', mode='a') as file:
    file.write('\nNew line added using with statement!')

with open(r'C:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day24\my_file.txt',mode='w') as file:
    file.write('This line overwrites the existing content.')

# if you open a file in write mode and the file does not exist, it will create a new file with the specified name.
with open(r'C:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day24\new_file.txt', mode='w') as file:
    file.write('This is a newly created file.')