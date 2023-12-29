sentence="This is a test sentence"
def table(x):
    for m in range(25):
        d=0
        for i in range(len(x)):
            if x[i].lower() == chr(ord('`')+m+1):
                d= d+1
        print(f"{chr(ord('`')+m+1)} - {d}")
table(sentence)


