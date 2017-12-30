L=float(input())
Done=False
while not Done:
    R=input()
    
    if R=="finshed":
        Done=True
    else:
        R=float(R)
        op=input()

        re=0 
         
        if op=="+":
            re=L+R
        elif op=="-":
            re=L-R
        elif op=="*":
            re=L*R
        elif op=="/":
            re=L/R
            
        print("="+str(re))
        L=re

