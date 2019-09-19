import json

def read_text(file):
    with open(file, 'r') as read_file:
        a = []
        b = []
        c = []
        d = []
        e = []
        while (True):
            line = read_file.readline()
            if not line:
                break
            item = [i for i in line.split(' ')]
            a.append(json.loads(item[0]))
            b.append(json.loads(item[1]))
            c.append(json.loads(item[2]))
            d.append(json.loads(item[3]))
            d.append(json.loads(item[4]))
        return a, b, c, d, e

a, b, c, d, e = read_text("../data/IrisDataset.txt")

