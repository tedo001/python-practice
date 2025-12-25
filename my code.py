set=["blue","blue","blue","blue","red","blue","blue","blue","red","",""]
balls=[]
get=[]
for i in range(len(set)):
    balls=set[i-1]

    if "red" in balls:
        print("red ball indice is",i-1)
        get= balls

    else:
        print("indice",i-1,"blue ball")

print(balls)