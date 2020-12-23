from datetime import datetime
if __name__ == '__main__':
    text = '20120920'
    y = datetime.strptime(text, '%Y%m%d')
    str = datetime.strftime(y, 'Date:	%Y年%m月%d日 GMT+8 23:59:59')
    print(str)
