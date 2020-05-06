s= "156444051@qq.com"
k=s.find("@qq")
if(k==-1):
    print("not find")
elif(k!=-1):
    print(k)
c=s.count("4")
print(c)
f=s.replace("@qq","@163")
print(s)
print(f)

m="010-21232312"
p=m.split("-")
print(p)
s="abc"
s=s.upper()
print(s)
s=s.isdigit()
print(s)