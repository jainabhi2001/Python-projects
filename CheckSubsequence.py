

def main():
 # Write code here
    V=input()
    N=int(input())
    B=[]
    for i in range(N):
        B.append(input())

    for ele in B:
        VIRUS=V
        flag=0
        for j in ele:
            if j in VIRUS:
                VIRUS=VIRUS[VIRUS.index(j)+1:]
                flag=1
            else:
                flag=0
                break
        if(flag==1):
            print("POSITIVE")
        else:
            print("NEGATIVE")


main()

