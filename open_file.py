#'w' write file
#'r' reading file
test_file = open('test.txt', 'w')
test_file.write('Hello world!\nPython')
test_file.close()
print(test_file)