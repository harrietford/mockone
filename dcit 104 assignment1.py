from audioop import avg


total=0
count=0
for i in range(1,10000):
    if i%2==0:
        total=total+i
        count=count+1
        avg=total/count
print(avg)
