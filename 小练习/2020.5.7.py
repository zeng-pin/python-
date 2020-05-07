c=1
# k=[]
# while (c<=100):
#     k.append(c)
#     c=c+1
# k.reverse()


# k=[y for x in range(1,10) for y in range(1,10)]
# print(k)

# t = [(2,3),(4,5)]
# print(t)

# t=(22,44,78,99)
# c=0
# while (c < len(t)):
#     print(t[c],end=" ")
#     c=c+1
# for x in t:
#     print(x,end=" ")

d={"a":123,"b":234,"c":"爱心"}
print(d)
p ={"height":1.75,"age":27,"name":"sarah"}
p["name"]="lili"
print(p["name"])
#字典的key必须是不可变的类型：字符串，元组，数字
d={(1,2):"hello"}
print(d[(1,2)])