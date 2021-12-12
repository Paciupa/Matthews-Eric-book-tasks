file_name = 'learning_python.txt'

with open(file_name, encoding='UTF-8') as txt_file_object:
    txt_file_contents = txt_file_object.read()
    print(txt_file_contents)

with open(file_name, encoding='UTF-8') as txt_file_object:
    for line in txt_file_object:
        print(line.rstrip())
print()

with open(file_name, encoding='UTF-8') as txt_file_object:
    txt_file_contents_as_list_of_lines = txt_file_object.readlines()
for line in txt_file_contents_as_list_of_lines:
    print(line.rstrip())
