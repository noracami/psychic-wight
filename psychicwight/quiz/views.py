from django.shortcuts import render, redirect
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


def filltruefalse(text):
    # [[1,2,3], [4,5,6], [1,2]]
    for q in text:
        if len(q) == 1:
            q[1:] = ["", "true_or_false"]
        elif len(q) == 2:
            q[2:] = ["true_or_false"]

    return text

# Create your views here.
def home(request):
    h = "%s%s%s" % ("○○部○○署", 104, "年度○○裝備檢查保養常識測驗")
    text2 = [{"name": "【車輛裝備】保養常識練習題庫（是非50題）", "section": 'car/1',},
             {"name": "【車輛裝備】保養常識練習題庫（選擇50題）", "section": 'car/2',},
             {"name": "【武器裝備】保養常識練習題庫（是非50題）", "section": 'weapon/1',},
             {"name": "【武器裝備】保養常識練習題庫（選擇50題）", "section": 'weapon/2',},
             {"name": "【通訊裝備】保養常識練習題庫（是非50題）", "section": 'communication/1',},
             {"name": "【通訊裝備】保養常識練習題庫（選擇50題）", "section": 'communication/2',},
             {"name": "【防彈裝備】保養常識練習題庫（是非21題）", "section": 'bulletproof/1',},
             {"name": "【防彈裝備】保養常識練習題庫（選擇21題）", "section": 'bulletproof/2',},
             {"name": "模擬測驗(隨機20題)", "section": 'random'},]
    return render(request, 'home.html', {
        "header": h,
        #"m": module_dir,
        #"text3": text3,
        #"l_t": l_t,
        "text2": text2,
        })


def maintenanceknowledge(request, section="", number=0, showall=False):
    ''' description '''
    h = "%s%s%s" % ("○○部○○署", 104, "年度○○裝備檢查保養常識測驗")
    if section == 'random' and number == 0:
        my_dir = "../static/quiz/random.csv"
    else:
        my_dir = "%s%s%s%s" % ('../static/quiz/', section, number, '.csv')
    text = parse_csv(my_dir)
    section_choice = {
        "car1": "【車輛裝備】保養常識練習題庫（是非50題）",
        "car2": "【車輛裝備】保養常識練習題庫（選擇50題）",
        "weapon1": "【武器裝備】保養常識練習題庫（是非50題）",
        "weapon2": "【武器裝備】保養常識練習題庫（選擇50題）",
        "communication1": "【通訊裝備】保養常識練習題庫（是非50題）",
        "communication2": "【通訊裝備】保養常識練習題庫（選擇50題）",
        "bulletproof1": "【防彈裝備】保養常識練習題庫（是非21題）",
        "bulletproof2": "【防彈裝備】保養常識練習題庫（選擇21題）",
        "random": "模擬測驗(隨機20題)",
    }
    #my_choice

    if section == 'random':
        text = filltruefalse(text)
        from random import shuffle
        shuffle(text)
        return render(request, 'random.html', {
            "showall": showall,
            "header": h,
            "text": text[:20],
            "l_t": 20,
            "true_or_false": "true_or_false",
            })

    elif number == '1':
        return render(request, 'true_or_false.html', {
            "showall": showall,
            "header": h,
            "t": section,
            "number": number,

            "m": my_dir,
            "text": text,
            "l_t": len(text),
            })
    elif number == '2':
        return render(request, 'multiple_choice_question.html', {
            "showall": showall,
            "header": h,
            "t": section,
            "number": number,

            "m": my_dir,
            "text": text,
            "l_t": len(text),
            })
    else:
        return redirect('home')
