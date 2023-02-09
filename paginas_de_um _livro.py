x = int(input())
t = 0
y = range(1, x+1)

for i in y:
    i = str(i)
    t = len(i) + t
        
print(t)
