# TTS (Text To Speech)
# pip install gTTS
# pip istall playsound
from gtts import gTTS
from playsound import playsound

text = 'Hi, 구자인입니다.'

tts = gTTS(text=text, lang='ko', slow=False)
tts.save('./studyPython/output/hi.mp3')
print('완료!')
playsound('./studyPython/output/hi.mp3')
print('음성출력 완료!')