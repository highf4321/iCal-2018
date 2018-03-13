# from requests_html import HTML
# coding= utf-8
from bs4 import BeautifulSoup
import re
from icalendar import Calendar, Event
from datetime import datetime

Week = ('一', '二', '三', '四', '五', '六', '日')
Time=[(datetime(2018, 2, 26, 8, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 9, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 10, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 11, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 14, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 15, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 16, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 17, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 19, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 26, 19, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
)
,(
datetime(2018, 2, 27, 8, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 9, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 10, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 11, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 14, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 15, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 16, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 17, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 19, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 27, 19, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
),(
datetime(2018, 2, 28, 8, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 9, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 10, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 11, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 14, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 15, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 16, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 17, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 19, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 2, 28, 19, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
),(
datetime(2018, 3, 1, 8, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 9, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 10, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 11, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 14, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 15, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 16, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 17, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 19, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 1, 19, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
),(
datetime(2018, 3, 2 8, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 9, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 10, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 11, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 14, 30, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 15, 20, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 16, 10, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 17, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 19, 00, tzinfo=pytz.timezone("Asia/Shanghai")),
datetime(2018, 3, 2 19, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
)]

def main():
    code = getHTMLText()
    infoDictList = []
    parser(code, infoDictList)
    # print(infoDictList)
    # for item in infoDictList:
    #     print(item)
    make_cal(infoDictList)
    print("end")


def getHTMLText():
    with open('/home/fengkx/ical/html.html', 'r', encoding='gb2312') as f:
        doc = f.read()
        return doc


def parser(doc, infoDictList):

    soup = BeautifulSoup(doc, 'html.parser')
    tables = soup.find_all('table')
    tab = tables[0]
    table = []
    for i in range(len(tab.find_all('tr'))):
        tr = tab.find_all('tr')[i]
        for j in range(len(tr.find_all('td'))):
            cell = tr.find_all('td')[j].getText().split()
            if len(cell):
                if len(cell) > 1:
                    table.append(cell)
    # print(table)
    lessonList=[]
    for lesson in table:
        # print(lesson)
        lessonList.append(lesson)
        # infoDict.update({'课程名称': lesson[0]})
    # print(lessonList)
    for lesson in lessonList:
        # print(lesson)
    # for i in range(len(lesson)):
        infoDict={}
        infoDict.update({'课程名称':lesson[0]})
        # print(infoDict)
        infoDict.update({'课程类型': lesson[1]})
        infoDict.update({'星期': Week.index(lesson[2][1])+1})
        rex = re.compile(r'第.*节')
        count = (rex.findall(lesson[2])[0])
        length = len(count)
        if 3 < length < 6:
            infoDict.update({'节数': (int(count[1]), int(count[3]))})
        elif length <= 3:
            infoDict.update({'节数': (int(count[1]),)})
        else:
            infoDict.update({'节数': (int(count[1]), int(count[3:5]))})
        # print(lesson[2])
        infoDict.update({'周次': (abs(eval(lesson[2][-6:-2]))+1)})
        infoDict.update({'授课教师': lesson[3]})
        try:
            infoDict.update({'上课地点': lesson[4]})
        except:
            continue
        infoDictList.append(infoDict)
        print(infoDict)
def make_cal(infoDictList):
    cal=Calendar()
    event1=Event()
    i=0
    for j in infoDictList[i][节数]:    
        event1.add('summary',infoDictList[i]['课程名称'])
        event1.add('location',infoDictList[i]['上课地点'])
        event1.add('description',infoDictList[i]['课程类型']+'\n'+infoDictList[i]['授课教师'])
        event1.add('dtstart',Time[infoDictList['星期'-1]][j-1])
        event1.add




if __name__ == '__main__':
    main()
