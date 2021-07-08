def mode(data):
    count = 0
    dic = {}
    compare = 0
    result = 0

    for i in data:
        if i not in dic:
            dic[i] = 0
            for j in data:
                if j == i:
                    dic[i] += 1
    for key, value in dic.items():
        if value > compare:
            compare = value
            result = key

    return result

