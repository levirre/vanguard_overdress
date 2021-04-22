#setparse.py
import os 
import sys
import subprocess
import time
import hashlib
#sed 's/regex/replace/' match regex 's/regex//;s/regex//;'multiple matches
#Card No.|Name|Grade|Nation|Type|Rarity
#curl https://cardfight.fandom.com/wiki/D_Booster_Set_01:_Genesis_of_the_Five_Greats?action=edit | grep '{{CardList|D-BT*' | sed 's/{{CardList|//;s/..$//;s/ /_/g' | awk -F'|' 'BEGIN{OFS=FS} {if ($2) gsub(/ /,"_")} {if(val=="") print{"empty"}} {print $0}' | tr '/' '-' > D-BT01.txt
#$1 = Card number in set
#$2 = Card name
#$3 = Card grade
#$4 = Card clan
#$5 = Card type
#$6 = Card rarity

#D-BT[num].txt
#Create url from $2
# awk -F'|' '{print $2}' D-BT01.txt | sed 's/ /_/g'  replace spaces with _
# awk -F'|' '{print $1}' D-BT01.txt | tr '/' '-'  
#D-BT01-001EN-RRR_(Sample).png md5hash this to get sub directory for url
#example url #https://static.wikia.nocookie.net/cardfight/images/8/80/D-BT01-001EN-RRR_%28Sample%29.png
#card_string = "D-BT01-001EN-RRR_(Sample).png"

#print(url)
#curl -o 'D-BT01-001EN-RRR_(Sample).png' 'https://static.wikia.nocookie.net/cardfight/images/8/80/D-BT01-001EN-RRR_%28Sample%29.png'

###### MAKE SET #################

## RUN THIS CURL FIRST ##

#URL_SOURCE= ""
#SET = ""
#curl $URL_SOURCE | grep '{{CardList*' | sed 's/{{CardList*|//;s/..$//;s/ /_/g' | tr '/' '-' | cut -d "|" -f 2-

#bash = ["touch ", set_name]
#subprocess.Popen(bash)
##############################

#REPLACE WITH NEEDED SET NAME
#text = 'D-SD05.txt'
#set_name = text.split('.')[0]
#text = 'test.txt'
#f = open(text,'r')
#content = f.read().splitlines()
#print(content)



####MAKE DIR ################
#def createSetFolder(){
#    bash = ["mkdir","img/" + text.split('.')[0]]
#    subprocess.Popen(bash)
#    bash = ["touch", "img/" + set_name + "/missing.txt"]
#    subprocess.Popen(bash)
#    time.sleep(2)

#}
#
############################



def isblank(card):
    if card[5].find('+'):
        card[5]= card[5].split('+')[0]
    if card[5] == "":
        card_string = card[0] + "EN" + card[5] + "_(Sample).png"
    else:
        card_string = card[0] + "EN-" + card[5] + "_(Sample).png"

def isblankJP(card):
    try:
        rarity=card[5]
      
    except:
        rarity=""
    finally:
        if rarity.find('+'):
            rarity= rarity.split('+')[0]
        if rarity == "":
            card_string = card[0] + rarity + "_(Sample).png"
        else:
            card_string = card[0] + "-" + rarity + "_(Sample).png"
        return card_string


def en_card_string_builder(card_string_builder):
    card_string = isblank(card_string_builder)
    #card_string = card_string_builder[0] + "EN-" + card_string_builder[5] + "_(Sample).png"
    
    image = hashlib.md5(card_string.encode())
    image_dir = image.hexdigest() 
    sub_dir = image_dir[0] + "/" + image_dir[0:2] + "/"
    url = ("https://static.wikia.nocookie.net/cardfight/images/" + sub_dir + card_string.split('_')[0]  + "_%28Sample%29.png")
    return url

def jp_card_string_builder(card_string_builder):
    card_string = isblankJP(card_string_builder)
    print(card_string_builder[0])
    image = hashlib.md5(card_string.encode())
    image_dir = image.hexdigest() 
    sub_dir = image_dir[0] + "/" + image_dir[0:2] + "/"
    url = ("https://static.wikia.nocookie.net/cardfight/images/" + sub_dir + card_string.split('_')[0]  + "_%28Sample%29.png")
    return url
##print(range(len(content)))
def construct(content,set_name):
    m = open('img/' + "D-BT01" + '/missing.txt','w')
    #print(m)
    for i in range(len(content)):
        #print(content[i])
        card_string_builder = content[i].split("|")
        #print(card_string_builder[1])

        url = jp_card_string_builder(card_string_builder)
        #   0               1               2           3               4           5
        #['D-BT01-001', 'Vairina_Valiente', '3', 'Dragon_Empire', 'Persona_Ride', 'RRR']
        #print(card_string_builder)
        #print(card_string_builder[0] + "EN-" + card_string_builder[5] + "_(Sample).png")

        print(url)
        bash = ["curl","-o","img/" + set_name +"/"+ card_string_builder[0] +  ".png",url]
        print(bash)
        subprocess.Popen(bash)

        if(card_string_builder[1] == ""):
            print(content[i])
            m.writelines(content[i] + "\n")
    m.close()

    

#time.sleep(2)
#bash = ["mv ",text,"img/" + set_name +"/"]
#subprocess.Popen(bash)