from gtts import gTTS
import os
tts = gTTS(text="xin chao toi ten la gigi", lang = 'vi')
tts.save("alien.mp3")

os.system("start alien.mp3")