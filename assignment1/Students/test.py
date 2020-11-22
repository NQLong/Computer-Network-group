# import threading
# import time
# threads = []
# def countdown(*num):
#     print(num)
#     for i in range(*num):
#         time.sleep(1)

# for i in range(15,5,-3):
#     threads += [threading.Thread(target = countdown,args=[i])]
#     threads[-1].start()
    

# for i in threads:

#     i.join()
#     print(i)
    
a = {1:12}
print(a.get(1))