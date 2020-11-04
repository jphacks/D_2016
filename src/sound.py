import winsound

import text_generator


def play_sound():
    with open("test.wav", "rb") as f:
        data = f.read()
    winsound.PlaySound(data, winsound.SND_MEMORY)


def need_to_sound() -> bool:
    """通知を送る条件を満たす場合True、ほかはFalse
    """
    # TODO: 通知が必要な条件を記入
    return False


if __name__ == '__main__':
    play_sound()
