""" This code takes 
    i. first line as a string/combination of a virus named "coronavirus"
    ii. second line as  "N" number of patients 
    iii. rest "N" number of lines takes the patient's report content (which has some sequence of characters)
    Note: We need to tell wether the patients's report sequence is a subsequence of "coronavirus".I f yes print "POSITIVE" else "NEGATIVE"

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

