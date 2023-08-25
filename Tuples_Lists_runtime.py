# Tuples and lists comparison runtime
import time

a = 1
list1 = []

while a < 10000:
    list1.append(a)
    a += 1

start_time_tuple = time.time()

tuple1 = (0, )

b = 1

while b < 10000:
    tuple2 = (b, )
    tuple1 += tuple2
    b += 1

s1 = time.process_time()
for x in list1:
    print(x)
e1 = time.process_time()

s2 = time.process_time()
for x in tuple1:
    print(x)
e2 = time.process_time()

run_time1 = e1-s1
run_time2 = e2-s2


print("runtime list", run_time1)
print("runtime tuple", run_time2)

list = []

for i in range(1000):
    list.append(i)

print(list)

