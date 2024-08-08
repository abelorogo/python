file= open('abel.txt' )
# print(file.readline())
# print('\n')
# print(file.readline())

# 
print(file.read())
print('\n')
for lines in file.readlines():
    print(lines)