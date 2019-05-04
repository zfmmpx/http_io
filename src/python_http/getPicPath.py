import os


def GetPath():
  print('aa')
  print('bb')
  return os.path.join(path, 'assets')

path = os.path.dirname(os.path.dirname(__file__))
# pic_path = os.path.join(path, 'assets')
pic_path = GetPath()

file_list = os.listdir(pic_path)
pic_list = []
for file in file_list:
    pic_list.append(os.path.join(pic_path, file))
for f in pic_list:
    print(f)