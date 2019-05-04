import os


path = os.path.dirname(os.path.dirname(__file__))
pic_path = os.path.join(path, 'assets')

file_list = os.listdir(pic_path)
for file in file_list:
    print(os.path.join(pic_path, file))

# print(file_list)