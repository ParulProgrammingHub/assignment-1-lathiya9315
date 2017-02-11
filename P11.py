p=float(raw_input("Enter The Principal Amount "))
t=float(raw_input("Enter The Time"))
r=float(raw_input("Enter The Interest Rate "))
n=float(raw_input("Number Of Time Per Year Rate Is Compounded "))
ir=r/100
a=1+ir/n
b=n*t
def cm_in(p,t,ir):
    t=p*a**t
    print("Total Amount (p+i)=%f"%(t))
cm_in(p,t,ir)
