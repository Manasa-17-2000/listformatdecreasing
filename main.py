a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))
d = int(input("enter the 4th number : "))

list=[]
list.append(a)
list.append(b)
list.append(c)
list.append(d)

list.sort(reverse=True)
print(list)
print(list[0],">",list[1],">",list[2],">",list[3])