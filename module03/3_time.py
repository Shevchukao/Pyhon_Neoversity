import time

now = time.time()  # 1761748238.809042 in seconds
print("time in seconds:", now)
rnow = time.ctime(now)
print("readable time:", rnow)

t1 = time.struct_time([2023, 12, 1, 12, 35, 45, 1, 125, -1])  # using in database
print(t1)


print(time.time())
time.sleep(10)  # pause the execution of the program for 10 seconds
print(time.time())

start = time.perf_counter()  # more perfect count than time.time
time.sleep(10)
end = time.perf_counter()
print(end - start)  # differences in time
