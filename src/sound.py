import winsound
import win32com.client
# 自前ライブラリ
import text_generator


def play_sound(txt):
    sapi = win32com.client.Dispatch("SAPI.SpVoice")
    cat  = win32com.client.Dispatch("SAPI.SpObjectTokenCategory")
    cat.SetID(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False)
    v = [t for t in cat.EnumerateTokens() if t.GetAttribute("Name") == "Microsoft Sayaka"]
    if v:
        oldv = sapi.Voice
        sapi.Voice = v[0]
        sapi.Speak(txt)
        sapi.Voice = oldv

def need_to_sound() -> bool:
    """通知を送る条件を満たす場合True、ほかはFalse
    """
    # TODO: 通知が必要な条件を記入
    return False


if __name__ == '__main__':
    txt = "test"
    play_sound(txt)
