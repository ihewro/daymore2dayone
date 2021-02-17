from datetime import datetime
import re

import_file_path = "/Users/hewro/Desktop/test.txt"
export_file_path = "/Users/hewro/Desktop/dayone_out.txt"

# 如果上一行是日期，紧邻的下一行也是日期，并且两个时间戳一致则该行日期不再录用
last_timestamp = 0.0

repeat_time = 0
day_cout = 0


def parse2time(title):
    global last_timestamp, repeat_time, day_cout
    y = datetime.strptime(title, '%Y年%m月%d日')
    curre_timestam = y.timestamp()
    if curre_timestam == last_timestamp:
        repeat_time = repeat_time + 1
        # print("repart time" + title)
        return ""
    else:
        last_timestamp = curre_timestam
        day_cout = day_cout + 1
        str = datetime.strftime(y, '	Date:	%Y年%m月%d日 GMT+8 23:59:59')
        return str


def checkIsDate(content):
    content = content.strip()
    ret = re.match(r'(\d{4}年\d{1,2}月\d{1,2}日)', content)
    if ret is not None:
        content = parse2time(ret.group(1))
        if content is "":
            return "----------分割线-------\n"
        else:
            return "\n"+content + "\n\n\n"
    else:
        return content + "\n"


if __name__ == '__main__':
    f_open = open(import_file_path)
    f_write = open(export_file_path, 'a')
    # 对每一行文字进行扫描
    line = f_open.readline()
    while line:
        # 匹配时间的正则表达式，如果匹配成功，修改为day one的时间戳
        content = checkIsDate(line)
        # print(content)
        f_write.write(content)
        line = f_open.readline()
    f_open.close()
    f_write.close()

    print("repeat_time" + str(repeat_time))
    print("day_count" + str(day_cout))
