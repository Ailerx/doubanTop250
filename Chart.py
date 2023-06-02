import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as ticker
rcParams['font.family'] = 'SimHei'  # 将字体设置为中文SimHei


def Main_Chart1():
    data = []
    # 打开文本文件并逐行读取数据
    with open('films.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            # 去除空格和换行符，并使用逗号将数据拆分成列表
            values = line.strip().split(',')
            appraise_num = int(values[5][:-3])
            # print(appraise_num)
            # 创建一个字典，用于存储每行数据的不同字段
            item = {
                'position': values[0],
                'name': values[1],
                'director': values[2],
                'actor':values[3],
                'score': values[4],
                'appraise_num': appraise_num
            }
            # 将字典添加到列表中
            data.append(item)
    name = [movie['name'] for movie in data]
    print(name)
    score = [movie['score'] for movie in data]
    new_score = list(map(float, score))
    print(score)
    appraise_ = [movie['appraise_num'] for movie in data]
    # appraise_ = [movie['appraise_num'] for movie in data]
    new_a = []
    new_appraise = []
    for num in appraise_:
        str_num = str(num)[:-3]  # 取出除最后三位外的其他位数
        new_a.append(int(str_num))
    print(new_a)
    for i in new_a:
        if i % 10 > 4:
            if len(str(i)) == 4:
                i = int(str(i)[:3]) + 1
                new_appraise.append(i)
            elif len(str(i)) == 3:
                i = int(str(i)[:2]) + 1
                new_appraise.append(i)
        elif len(str(i)) == 4:
            i = int(str(i)[:3])
            new_appraise.append(i)
        elif len(str(i)) == 3:
            i = int(str(i)[:2])
            new_appraise.append(i)
    fig, c1 = plt.subplots(figsize=(22, 13), dpi=67)
    fig.suptitle("豆瓣电影")
    line1,=c1.plot(name, new_score, label="评分", color='black')
    c1.set_xticks(range(len(name)))
    c1.set_xlabel("电影名", labelpad=0.4)
    c1.set_xticklabels(name, rotation=70)
    c1.set_ylabel('分数', fontsize=15)
    c2 = c1.twinx()
    line2,=c2.plot(name, new_appraise, label="评价数",color="skyblue")
    c2.set_ylabel('评价数(万)', fontsize=12)

    plt.grid()
    plt.legend(handles=[line1,line2])
    plt.show()


if __name__ == '__main__':
    Main_Chart1()
