import logging
import threading
import time
import keyboard

import activity_log
import notification
import sound
import text_generator

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

stop = False  # スレッドの終了用
interval = 2  # 記録の間隔
working_state_list = ["start",
                      "terminate",
                      "cheer",
                      "praise",
                      "idle"]
working_state = "idle"


def log_activity_to_file(previous_program_list, current_program_list,
                         skip_duplicate=True):
    global working_state

    # プログラムの起動と終了を検知
    current_program_list = activity_log.get_all_windows()
    started = activity_log.get_title_of_started_program(
        previous_program_list=previous_program_list,
        current_program_list=current_program_list)
    terminated = activity_log.get_title_of_terminated_program(
        previous_program_list=previous_program_list,
        current_program_list=current_program_list)

    if terminated:
        working_state = "terminate"
        title = terminated
        state = "T"
        activity_log.print_to_file(title, state)
        event_notification.set()
        event_voice.set()
        
    if started:
        working_state = "start"
        title = started
        state = "S"
        activity_log.print_to_file(title, state)
        activity_log.set_start_word_num(title.split()[0])
        event_voice.set()
        event_notification.set()

    working_time = activity_log.get_working_time_on_current_window(interval=2)
    logging.debug("working_time: " + str(working_time))
    thresholds = [3600 for _ in range(8)]  # 1～8時間
    for threshold in thresholds:
        if threshold <= working_time < threshold + interval:
            working_state = "cheer"
            event_voice.set()
            event_notification.set()

    
    # アクティブウィンドウの記録
    title = activity_log.get_title_of_active_window(skip_duplicate)
    state = "A"
    if title:
        activity_log.print_to_file(title, state)

    title = activity_log.get_active_window_title() 
    if len(title.split()) < 2:
        return 
    elif ".docx" in title.split()[0] and title.split()[-1] == "Word":
        start_word_num = activity_log.get_start_word_num()
        finish_word_num = activity_log.get_finish_word_num(title.split()[0])
        need_to_notify = notification.need_to_notify(start_word_num,finish_word_num)
        if need_to_notify == True:
            working_state = "praise"
            event_notification.set()
            event_voice.set()
            

def worker_log(event_log):
    """ログ記録のためのworker
    """
    previous_program_list = activity_log.get_all_windows()
    while not stop:
        # event.set が実行されるまで待機
        event_log.wait()
        event_log.clear()
        logging.debug('logging start')

        current_program_list = activity_log.get_all_windows()
        log_activity_to_file(previous_program_list,
                             current_program_list)
        previous_program_list = current_program_list

        logging.debug('logging end')


def worker_voice(event_voice):
    """音声再生のためのworker
    """
    while not stop:
        # event.set が実行されるまで待機
        event_voice.wait()
        event_voice.clear()
        logging.debug('voice start')
        text = text_generator.generate_text(working_state)
        # time.sleep(3)
        sound.play_sound(text)
        logging.debug('voice end')


def worker_notification(event_notification):
    """通知のためのworker
    """
    global working_state
    while not stop:
        # event.set が実行されるまで待機
        event_notification.wait()
        event_notification.clear()
        logging.debug('notify start')
        text = text_generator.generate_text(working_state)
        img_path = notification.generate_path(working_state)
        notification.notify(text, img_path)
        logging.debug('notify end')
        if working_state == "praise": 
            title = activity_log.get_active_window_title() 
            activity_log.set_start_word_num(title.split()[0])
            working_state = "idle"

def worker_main(event_log, event_voice, event_notification):
    """処理の中心となるworker
    """
    global stop
    global working_state

    logging.debug('start')
    print(stop)
    while not stop:
        if keyboard.is_pressed("q"):
            logging.debug("q is pressed, program end")
            exit()
            stop = True

        time.sleep(interval)
        event_log.set()
        logging.debug("event_log.set()")
        logging.debug("working_state: " + working_state)

        need_to_play_voice = sound.need_to_sound()
        if need_to_play_voice:
            event_voice.set()
            logging.debug("event_voice.set()")

        need_to_notify = notification.need_to_notify(-1,-1)
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
