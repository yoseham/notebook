import json

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def read_text(file):
    with open(file, 'r') as read_file:
        a = []
        b = []
        c = []
        d = []
        while (True):
            line = read_file.readline()
            if not line:
                break
            item = [i for i in line.split(' ')]
            a.append(json.loads(item[0]))
            b.append(json.loads(item[1]))
            c.append(json.loads(item[2]))
            d.append(json.loads(item[3]))
        return a, b, c, d

def show(a,cut_num,title):
    name = [chr(i) for i in range(65,91)]
    count_a = [0]*cut_num
    min_a = min(a)
    max_a = max(a)
    cut_dist = (max_a-min_a)/cut_num

    for ai in a:
        id = int((ai-min_a)/cut_dist)
        if id==cut_num :
            id-=1
        count_a[id]+=1

    count_a = [ i/len(a) for i in count_a]
    print(count_a)
    x = name[:cut_num]
    label = "\n".join([str(x[i]) + ': [' + str(round(min_a+i*cut_dist,2)) +',' +str(round(min_a+(i+1)*cut_dist,2)) +')' for i in range(cut_num)])
    plt.bar(x=x,height=count_a,label=label)
    plt.title(title)
    plt.legend(loc='upper right')
    plt.show()

def show_1(a,cut_num,plt,title):
    name = [chr(i) for i in range(65,91)]
    count_a = [0]*cut_num
    min_a = min(a)
    max_a = max(a)
    cut_dist = (max_a-min_a)/cut_num

    for ai in a:
        id = int((ai-min_a)/cut_dist)
        if id==cut_num :
            id-=1
        count_a[id]+=1

    count_a = [ i/len(a) for i in count_a]
    print(count_a)
    x = name[:cut_num]
    label = "\n".join([str(x[i]) + ': [' + str(round(min_a+i*cut_dist,2)) +',' +str(round(min_a+(i+1)*cut_dist,2)) +')' for i in range(cut_num)])
    plt.bar(x=x,height=count_a,label=label)

    plt.legend(loc='upper right')

a, b, c, d = read_text("../data/IrisDataset.txt")

cut_num=5

# show(d,cut_num,'forth column')
# fig = plt.figure(figsize=(20,5))
# for i in range(5):
#     ax = plt.subplot(1,5,i+1)
#     show_1(d,cut_num+i,ax)
# plt.show()


# plt.scatter(range(150),a)
# plt.hist(a,bins=20,normed=True)
# sns.distplot(a,20)
# plt.show()



# 第一个图

# cut_num = 3
# fig, axes = plt.subplots(2,5,figsize=(20,10))
# plt.title("first column") # 标题
# sa = pd.Series(a);
# for i in range(5):
#     axes[0][i].hist(a, bins=cut_num + 2 * i, edgecolor="black",normed=150)

# sa.plot(kind='kde')
# plt.subplots_adjust(wspace=0, hspace=0)
# sns.distplot(a,5)
# plt.show()

# fig, axes = plt.subplots(2,2, figsize=(5, 5),sharey=True,sharex=True)
#
sorted_a = sorted(b)
part_a1 = sorted_a[:int(len(a) / 2)]
part_a2 = sorted_a[int(len(a) / 2):]
plt.figure(figsize=(15,5))
ax0 = plt.subplot(1,3,1)
show_1(sorted_a,cut_num,ax0,'1')
ax1 = plt.subplot(1,3,2)
show_1(part_a1,cut_num,ax1,'2')
ax2 = plt.subplot(1,3,3)
show_1(part_a2,cut_num,ax2,'3')
plt.show()
#
# axes[0,0].hist(part_a1, bins=30, edgecolor='black')
# axes[0,1].hist(part_a2, bins=30, edgecolor='black')
#
part_a3 = b[:int(len(a) / 2)]
part_a4 = b[int(len(a) / 2):]
plt.figure(figsize=(15,5))
ax0 = plt.subplot(1,3,1)
show_1(b,cut_num,ax0,'1')
ax1 = plt.subplot(1,3,2)
show_1(part_a3,cut_num,ax1,'2')
ax2 = plt.subplot(1,3,3)
show_1(part_a4,cut_num,ax2,'3')
plt.show()
#
# axes[1,0].hist(part_a3, bins=30, edgecolor='black')
# axes[1,1].hist(part_a4, bins=30, edgecolor='black')
#
#
# plt.show()
#
# plt.hist(a,bins=30,edgecolor="black")
# plt.show()
