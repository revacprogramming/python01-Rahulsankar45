# Files

filename = "dataset/mbox-short.txt"
str1 = "hello"
str2 = "rahul"
r = str1 + str2
print(r)
fruit = "banana"
letter = fruit[4]
print(letter)
x = 4
r = fruit[x-1]
print(r)
x = "rahul"
print(len(x))
fruit = 'reva'
index = 0
while index <len(fruit):
  letter = fruit[index]
  print(index, letter)
  index = index +1
fruit ="banana"
for letter in fruit :
  print(letter)
x = "banana"
count =0
for letter in x:
  if letter == 'a':
    count = count +1
print(count)
s = "rahul jain"
print(s[0:6])
a = "hello"
b = a + "hello"
print(b)
n = ("REVa")
a = n.find('a')
print(a)
greet = ' HELLO BOB '
r= greet.lower()
print(r)
p = greet.replace('BOB','john')
print(p)
s = greet.lstrip()
print(s) 



x ='Reva cse@bangalore new' 
y =x.find('@')
print(y)
sopp = x.find(' ',y)
print(sopp)
host = x[y+1:sopp]
print(host)

z = ["rohit,virat,rahul"]
for x in z :
  print('all the best',z)
