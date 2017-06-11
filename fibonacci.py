def fibnum():
    N=input("How many Fibonacci sequence numbers do you want? ")
    a,b=0,1
    for i in range(int(N)):
        a,b=b,a+b
        print (a)
fibnum()
