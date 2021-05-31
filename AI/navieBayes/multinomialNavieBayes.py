import json

d = []
p = {}
feature_names = []


def convertVectorPredict(x):
    vt = [0]*len(feature_names)
    spl = x.split()
    for w in spl:
        if w in feature_names:
            idx = feature_names.index(w)
            vt[idx] += 1
    return vt


def predict(txt):
    x = convertVectorPredict(txt)
    prd = {}
    s = 0
    print("predict")
    for i in p:
        s += p[i]

    print(s)
    for ik in p:
        m = p[ik] / s
        i = int(ik)
        sl = sum(d[i])
        for j in range(len(x)):
            if x[j] > 0:
                print(d[i][j])
                m *= (d[i][j] / sl) ** x[j]
        prd[i] = m
    cls = max(prd, key=prd.get)
    print(prd)
    return cls, prd


def load_modal():
    filename = "AI/navieBayes/mnb.txt"
    for line in open(filename):
        w = line.split(": ")
        val = json.loads(": ".join(w[1:]));
        if w[0] == "p":
            global p
            p = val
        elif w[0] == "d":
            global d
            d = val
        elif w[0] == "feature_name":
            global feature_names
            feature_names = val

    print("Modal navibayes")
    print(feature_names)
