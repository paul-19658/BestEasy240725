import threading
import time

# 每1秒加1
def job1(num):
    while True:
        num += 1
        print('{} is running >> {}'.format(threading.current_thread().name, num))
        time.sleep(1)

# 每2秒加2
def job2(num):
    while True:
        num += 2
        print('{} is running >> {}'.format(threading.current_thread().name, num))
        time.sleep(2)

# 线程1，一秒加一
new_job1 = threading.Thread(target=job1, name='Add1', args=(100,))
new_job1.start()

# 线程2，两秒加二
new_job2 = threading.Thread(target=job2, name='Add2', args=(1,))
# 设置为守护线程
new_job2.daemon=True
new_job2.start()

# 主线程等待3秒
time.sleep(3)
print('{} Ending'.format(threading.current_thread().name))

# 一个是守护线程，一个不是
# 可以看到，上面的主线程结束后，两个子线程并没有结束，这也表明了守护线程会等到非守护线程执行完毕后再被杀死。

# 需要注意的是， setDaemon 必须写在 start 方法之前。