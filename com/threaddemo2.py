from time import ctime, sleep
import threading
import numpy as np

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(3)

def music2():
    for i in range(2):
        print("I was listening to. %s" %  ctime())
        sleep(1)

def movie(func):
    for i in range(4):
        print("movies!%s %s" % (func, ctime()))
        sleep(2)


def thread_(urls):
    a = []
    for url in urls:
        th = threading.Thread(target=music, args=(url,))
        a.append(th)

    for i in a:
        i.start()
    for i in a:
        i.join()


if __name__ == '__main__':
    # threads = []
    # t1 = threading.Thread(target=music, args=(u'爱情买卖',))
    # threads.append(t1)
    # t2 = threading.Thread(target=movie, args=(u'阿凡达',))
    # threads.append(t2)
    #
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    # print("all over %s" % ctime())
    thread_(np.arange(50))
