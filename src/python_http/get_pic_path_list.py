import os
from keyword import kwlist


def get_pic_source_dir():
    curr_dir = os.path.dirname(os.path.dirname(__file__))
    pic_source_dir = os.path.join(curr_dir, 'assets')
    return pic_source_dir

pic_name_list = os.listdir(get_pic_source_dir())

def get_pic_path_list():
    pic_path_list = []
    for pic_name in pic_name_list:
        pic_path_list.append(os.path.join('assets', pic_name))
    return pic_path_list


# def get_pic_full_path_list():
#     pic_full_path_list = []
#     for pic_name in pic_name_list:
#         pic_full_path_list.append(os.path.join(get_pic_source_dir(), pic_name))
#     return pic_full_path_list

