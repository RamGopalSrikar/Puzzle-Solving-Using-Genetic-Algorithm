import json


def fitnessEval(obj):
    # { puzzle : [], length : l, width : w }
    # print(jsonInput)
    pieces = obj['puzzle']
    l = obj['length']
    w = obj['width']
    #print(pieces, l, w)
    if len(pieces) == 0 or l == None or l == 0 or w == None or w == 0:
        return json.dumps({'fitness': 'input error'})
    frame = [[1 for _ in range(l)] for _ in range(w)]

    count = 0
    for p in pieces:
        count += 1
        for j in range(p[1], p[1] + int(p[3])):
            for i in range(p[0], p[0] + int(p[2])):
                if 0<=i < l and 0<=j < w:
                    try:
                        frame[j][i] = 0
                    except:
                        print("i={},j={},l={},w={}".format(i,j,l,w))

    free_space = 0

    frame = frame[::-1]

    for i in frame:
        for k in i:
            free_space += k
    
    if "fitness" in obj:
        obj['fitness']=100-(free_space/(l*w) * 100)
    else:
        obj.update({'fitness': 100-(free_space/(l*w) * 100)})
# fitness = freespace / (l * w)
    
    # return free_space

