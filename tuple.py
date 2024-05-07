#biar bisa masukkin func pucntuation
import string                                
                             
fhand = open("the night we met.txt")
counts = dict()

for line in fhand:
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)

for key, val in lst[:6]:
    print(key,val)
            
            
            

a = "hi"
b = type(a)
print(b)        #output: string

a = ("hi",)
b = type(a)
print(b)        #output: tuple

a = (
    "hi",
    "hello"
)
c = ("hola")
a = list(a)
a.append(c)
a = tuple(a)
print(a)