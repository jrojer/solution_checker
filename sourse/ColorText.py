# Author: Rusanov jrojer Aleksei
# ColorText.py; 
# 2016-04-06 23:58; 



def RedText(text):
    blue_text = "<span style=\" font-size:9pt; font-weight:600; color:#ff0000;\" >"
    blue_text += text
    blue_text += "</span>"
    return blue_text

def BlueText(text):
    red_text = "<span style=\" font-size:9pt; font-weight:600; color:#0000ff;\" >"
    red_text += text
    red_text += "</span>"
    return red_text
def GreenText(text):
    green_text = "<span style=\" font-size:9pt; font-weight:600; color:#00ff00;\" >"
    green_text += text
    green_text += "</span>"
    return green_text

