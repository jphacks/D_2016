import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

stop = False  # スレッドの終了用


def worker_voice(event_voice):
    """音声再生のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_voice.wait()
        event_voice.clear()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker_notification(event_notification):
    """通知のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_notification.wait()
        event_notification.clear()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker_main(event_voice, event_notification):
    """処理の中心となるworker
    """
    global stop
    logging.debug('start')
    time.sleep(5)
    # event.waitにしたスレッドを実行
    event_voice.set()
    time.sleep(5)
    event_notification.set()
    time.sleep(5)
    event_voice.set()
    time.sleep(5)
    logging.debug('end')
    stop = True
    exit()


if __name__ == '__main__':
    event_voice = threading.Event()
    event_notification = threading.Event()

    thread_main = threading.Thread(
        name="thread_main",
        target=worker_main,
        args=(event_voice, event_notification, ))

    # メインスレッド以外はすべてデーモン化
    thread_voice = threading.Thread(
        name="thread_voice",
        target=worker_voice,
        args=(event_voice,))
    thread_voice.setDaemon(True)

    thread_notification = threading.Thread(
        name="thread_notification",
        target=worker_notification,
        args=(event_notification,))
    thread_notification.setDaemon(True)

    thread_main.start()
    thread_voice.start()
    thread_notification.start()
