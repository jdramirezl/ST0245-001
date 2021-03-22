def brokenKeyboard(text):
    from collections import deque
    l = deque()
    
    size = 0
    i, j = 0, 0 
    isStart = True
    while j < len(text):
        print(text[i:j])
        if text[j].isalpha() and ( j+1 == len(text ) or not text[j+1].isalpha()):
            if isStart:
                l.appendleft(text[i:j+1])
            else:
                l.append(text[i:j+1])
        elif text[j] == "[" :
            isStart = True
            i = j + 1
        elif text[j] == "]":
            isStart = False
            i = j + 1
        j += 1
    

    return "".join(list(l))

ans = brokenKeyboard("asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]dg")
if ans == "dddfgdfhgfhasdhghfdfhdgdg":
    print("xd")
else:
    print(ans)