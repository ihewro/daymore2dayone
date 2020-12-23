"""
day more -> day one
so you can use day more data to geZhi app or other app like bear
"""
import os
from datetime import datetime

day_more_path = "/Users/hewro/Downloads/daymore_20201223"
target_day_one_path = "/Users/hewro/Desktop/dayone/result.txt"
target_day_one_img_dir_path = "/Users/hewro/Desktop/dayone/photos"

img_file_list = []

data_map = {
}

img_map = {
}


def parse2time(title):
    print("title:" + title)
    y = datetime.strptime(title, '%Y%m%d')
    str = datetime.strftime(y, '	Date:	%Y年%m月%d日 GMT+8 23:59:59')
    return str


def create_one(m_title):
    # 根据title 解析出时间
    # 增加时间戳
    m_ret = parse2time(m_title)
    f_t = open(target_day_one_path, 'a')
    # f_t.write("\n\n")
    f_t.write(m_ret + "\n\n")  # 先写入标题

    for file in data_map[title]:
        path = day_more_path + "/" + file
        f = open(path)
        line = f.readlines()
        f_t.writelines(line)  # 在写入之前的文件
        f.close()

    # 判断是否有图片
    if title in img_map:
        for img_file in img_map[title]:
            f_t.write("![](photos/" + img_file + ")")
    f_t.write("\n\n")
    f_t.close()


def getTitleFromFileName(filename):
    file_name = filename[:-4]
    m_list = filename.split('_')
    m_title = file_name
    if len(m_list) == 1:
        pass
    else:
        m_title = m_list[0]
    return m_title


#
def inset2data_map(key, value):
    if key in data_map:
        pass
    else:
        data_map[key] = [value]


def inset2img_map(key, value):
    if key in img_map:
        img_map[key].append(value)
    else:
        img_map[key] = [value]


if __name__ == '__main__':
    entries = []
    ret = {
        "metadata": {
            "version": "1.0"
        },
        "entries": entries
    }
    # 扫描目录，获取整理的数据map
    g = os.walk(day_more_path)

    for path, dir_list, file_list in g:
        for file_name in file_list:
            # 获取文件内容和图片列表
            full_path = os.path.join(path, file_name)

            if full_path[-3:] == "txt":
                # 判断title 是否包含_x 这种数字
                title = getTitleFromFileName(file_name)
                inset2data_map(title, file_name)

            if full_path[-3:] == "jpg":
                title = getTitleFromFileName(file_name)
                inset2img_map(title, file_name)
                # 将图片指定目录下移动到

    print(len(data_map.keys()))
    # for title in data_map:
    #     print(title + "-------")
    #     create_one(title)
    #     # for file in data_map[title]:
    #     #     print("file:"+ file);
