from django.shortcuts import render
import os
import csv

def parse_csv(source_dir):
    module_dir = os.path.join(os.path.dirname(__file__), source_dir)
    with open(module_dir, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        i = 1
        text = []
        for row in spamreader:
            clist = []
            for s in row:
                for c in s.split(','):
                    if c == "":
                        pass
                    else:
                        clist += [c]
            i += 1
            text += [clist]

    return text

# Create your views here.
def home(request):
    h = "%s%s%s" % ("○○部○○署", 104, "年度○○裝備檢查保養常識測驗")
    text3 = parse_csv('../static/car1.csv')
    l_t = len(text3)
    return render(request, 'home.html', {
        "header": h,
        #"m": module_dir,
        "text3": text3,
        "l_t": l_t,
        })
    text = {
        "t1": "【車輛裝備】保養常識練習題庫（選擇50題）",
        "t2": "【車輛裝備】保養常識練習題庫（是非50題）",
        "t3": "【武器裝備】保養常識練習題庫（選擇50題）",
        "t4": "【武器裝備】保養常識練習題庫（是非50題）",
        "t5": "【通訊裝備】保養常識練習題庫（選擇50題）",
        "t6": "【通訊裝備】保養常識練習題庫（是非50題）",
        "t7": "【防彈裝備】保養常識練習題庫（選擇20題）",
        "t8": "【防彈裝備】保養常識練習題庫（是非20題）",
        "t9": "模擬測驗(隨機20題)",
    }
    text2 = ["【車輛裝備】保養常識練習題庫（選擇50題）", "【車輛裝備】保養常識練習題庫（是非50題）",
             "【武器裝備】保養常識練習題庫（選擇50題）", "【武器裝備】保養常識練習題庫（是非50題）",
             "【通訊裝備】保養常識練習題庫（選擇50題）", "【通訊裝備】保養常識練習題庫（是非50題）",
             "【防彈裝備】保養常識練習題庫（選擇20題）", "【防彈裝備】保養常識練習題庫（是非20題）",
             "模擬測驗(隨機20題)",]


def maintenanceknowledge(request, section="", number=0):
    ''' description '''
    h = "%s%s%s" % ("○○部○○署", 104, "年度○○裝備檢查保養常識測驗")
    my_dir = "%s%s%s%s" % ('../static/', section, number, '.csv')
    text = parse_csv(my_dir)
    section_choice = {
        "car1": "【車輛裝備】保養常識練習題庫（選擇50題）",
        "car2": "【車輛裝備】保養常識練習題庫（是非50題）",
        "weapon1": "【武器裝備】保養常識練習題庫（選擇50題）",
        "weapon2": "【武器裝備】保養常識練習題庫（是非50題）",
        "communication1": "【通訊裝備】保養常識練習題庫（選擇50題）",
        "communication2": "【通訊裝備】保養常識練習題庫（是非50題）",
        "bulletproof1": "【防彈裝備】保養常識練習題庫（選擇20題）",
        "bulletproof2": "【防彈裝備】保養常識練習題庫（是非20題）",
        "random": "模擬測驗(隨機20題)",
    }
    my_choice

    if number == '2':
        return render(request, 'multiple_choice_question.html', {
            "header": h,
            "t": section,
            "number": number,

            "m": my_dir,
            "text3": text,
            "l_t": len(text),
            })
    else:
        return render(request, 'home.html', {
            "header": h,
            "t": section,
            "number": number,

            "m": my_dir,
            "text3": text,
            "l_t": len(text),
            })
