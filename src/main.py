import logging
import threading
import time
import keyboard

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

stop = False  # スレッドの終了用


def worker_log(event_log):
    """ログ記録のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_log.wait()
        event_log.clear()
        logging.debug('logging start')
        time.sleep(0.5)
        logging.debug('logging end')


def worker_voice(event_voice):
    """音声再生のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_voice.wait()
        event_voice.clear()
        logging.debug('voice start')
        time.sleep(5)
        logging.debug('voice end')


def worker_notification(event_notification):
    """通知のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_notification.wait()
        event_notification.clear()
        logging.debug('notify start')
        time.sleep(3)
        logging.debug('notify end')


def worker_main(event_log, event_voice, event_notification):
    """処理の中心となるworker
    """
    global stop
    logging.debug('start')
    print(stop)
    while not stop:
        if keyboard.is_pressed("q"):
            logging.debug("q is pressed, program end")
            exit()
            stop = True

        time.sleep(2)
        event_log.set()
        logging.debug("event_log.set()")

        need_to_play_voice = keyboard.is_pressed("m")
        if need_to_play_voice:
            event_voice.set()
            logging.debug("event_voice.set()")

        need_to_notify = keyboard.is_pressed("n")
        if need_to_notify:
            event_notification.set()
            logging.debug("event_notification.set()")


if __name__ == '__main__':
    event_log = threading.Event()
    event_voice = threading.Event()
    event_notification = threading.Event()

    thread_main = threading.Thread(
        name="thread_main",
        target=worker_main,
        args=(event_log, event_voice, event_notification, ))

    # メインスレッド以外はすべてデーモン化
    thread_log = threading.Thread(
        name="thread_log",
        target=worker_log,
        args=(event_log,))
    thread_log.setDaemon(True)

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
    thread_log.start()
