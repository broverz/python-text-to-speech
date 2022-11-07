from gtts import gTTS
import os

x = input('Text :> ')
y = input('Lang(en or th) :> ')
text = x

audio = gTTS(text=text, lang=y, slow=False)
audio.save("example.mp3")

os.system("start example.mp3")