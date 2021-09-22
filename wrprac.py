from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("friend.txt", "r", encoding="utf-8") as f:
     lines = f.readlines()
     for line in lines[5:]:
         if '] [' in line:
             text += line.split('] ')[2].replace('ㅋ', '').replace('내가', '').replace('나는', '').replace('난', '').replace('나', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진\n', '').replace('너네', '').replace('웅', '').replace('응', '').replace('ㅌ', '').replace('ㅇㅇ', '').replace('https', '').replace('사진 30장', '').replace('30장', '').replace('다', '').replace('이', '').replace('도', '').replace('ㅎ', '')

# print(text)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Users/Bae Soyeon/AppData/Local/Microsoft/Windows/Fonts/yg-jalnan.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("another.png")