import re
from datetime import datetime
if __name__ == '__main__':
    text = '2015年6月24日'
    y = datetime.strptime(text, '%Y年%m月%d日')
    str = datetime.strftime(y, 'Date:	%Y年%m月%d日 GMT+8 23:59:59')
    print(y.timestamp())
    print(str)

    # print(re.match("(\d{4}年\d{2}月\d{2}日)", "2015年10月09日", flags=0))

