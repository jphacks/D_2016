# Windowsのpipが死んでいたので動かせなかったがMacでは動いているので大丈夫なはず

from gtts import gTTS
hoge = gTTS("Hello World")
hoge.save("sample.mp3")