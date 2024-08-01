import threading
import time

# 每1秒加1
def job1(num):
    while num < 105:
        num += 1
        print('{} is running >> {}'.format(threading.current_thread().name, num))
        time.sleep(1)
    print("job1 Endding")

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

# 主线程等待job1执行完成
new_job1.join()
print('{} Ending'.format(threading.current_thread().name))

