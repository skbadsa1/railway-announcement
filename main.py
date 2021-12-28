import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


# this function returns pydub audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined    

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1 is generate kripiya dhayen dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("21_hindi.mp3", format="mp3")
    
    # 2 is from city

    # 3 - generate se chal kar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("23_hindi.mp3", format="mp3")
    
    # 4 is via city

    # 5 -generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("25_hindi.mp3", format="mp3")

    # 6 - is to-city

    #7 - generate ko jane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("27_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - generate kuch hi samay me platfrom sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("29_hindi.mp3", format="mp3")
    
    
    # 10 is plat from number


    # 11 - generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("31_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        #2 generate from city
        textToSpeech(item['from'], '22_hindi.mp3')

        #4 generate via city
        textToSpeech(item['via'], '24_hindi.mp3')

        #6 - generate to-city
        textToSpeech(item['to'], '26_hindi.mp3')

        #8 generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '28_hindi.mp3')

        #10 generate platfrom number 
        textToSpeech(item['platform'], '30_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(21,32)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

    

if __name__ == "__main__":
    print("Generate Skeleton...")
    generateSkeleton()
    print("Now generating announcement...")
    generateAnnouncement("announce_hindi.xlsx")