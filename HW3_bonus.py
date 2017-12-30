def F2 (dim):
    return int(input("Enter a "+dim))

def F1(w):
    print("#"*w)

width=F2 ("width")
height=F2 ("height")
F1(width)
for h in range(2,height):
    print("#" + " "*(width-2) + "#")
F1(width)

