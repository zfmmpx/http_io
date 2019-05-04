import os


path = os.path.dirname(os.path.dirname(__file__))
pic_path = os.path.join(path, 'assets')

file_list = os.listdir(pic_path)
pic_list = []
for file in file_list:
    pic_list.append(os.path.join(pic_path, file))
