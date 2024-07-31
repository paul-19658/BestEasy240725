import os
import time


# 当文件夹内图片数量到达某个值 结束所有进程 设一个特殊的进程结束条件是这个 然后正常的16个线程都设为守护线程，
# 那能不能线程运行中进行参数调整 或者暂停然后进行参数调整

# 获得文件夹内图片数量
def fileNum(dirNum) -> int:
    path = f'../ImgGot{dirNum}'
    fileList = os.listdir(path)
    # print(len(fileList))
    return len(fileList)

def mainThread(dirNum):
    while fileNum(dirNum)<=12000:
        print('\n\n当前文件夹内图片数：{}/12000\n\n'.format(dirNum))
        time.sleep(10)
    print('\n\n任务完成！ 文件夹内图片数：{}/12000\n\n'.format(dirNum))


if __name__ == '__main__':
    # print(fileNum(7))
    dirNum=99

    if fileNum(7) > 12000:
        print()

