import winsound


def sound():
    with open("media/test.wav", "rb") as f:
        data = f.read()
    winsound.PlaySound(data, winsound.SND_MEMORY)


if __name__ == '__main__':
    sound()
