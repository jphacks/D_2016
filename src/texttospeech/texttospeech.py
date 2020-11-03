import winsound

with open("test.wav", "rb") as f:
    data = f.read()
    
winsound.PlaySound(data, winsound.SND_MEMORY)