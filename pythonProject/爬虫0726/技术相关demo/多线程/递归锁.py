import threading, time


def run1():
    lock.acquire()
    print("grab the first part data")
    global num
    num += 1
    lock.release()
    return num


def run2():
    lock.acquire()
    print("grab the second part data")
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)


if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.RLock()
    for i in range(3):
        t = threading.Thread(target=run3) # 3个run3的线程并行，所以需要外面这层锁
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)
