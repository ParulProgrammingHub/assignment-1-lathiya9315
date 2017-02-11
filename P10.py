def sp_in(p,t,r):
    s=float((p*r*t)/100)
    print("Simple Interest Is : ",s)
p=int(raw_input("Enter the Principal Amount : "))
r=int(raw_input("Enter Interest Rate (in %) : "))
t=int(raw_input("Enter The Time : "))
sp_in(p,t,r)
