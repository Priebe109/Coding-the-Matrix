def dict2list(dct, keyList): return [dct[keyList[i]] for i in range(len(keyList))]

def list2dict(L, keyList): return {x:y for (x,y) in zip(keyList, L)}

def listrange2dict(L): return {x:y for (x,y) in zip(range(len(L)), L)}