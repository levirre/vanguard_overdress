#!/bin/bash
#set_builder.sh
build_set() {
    
    read -p 'Paste Set URL Source: '  URL
    #echo Entered: 
    #echo $URL
    ##
    
    LIST=$(curl $URL | grep '{{CardList*' | grep -v 'header\|footer'| sed 's/..$//;s/ /_/g' | cut -d "|" -f 2- | tr '/' '-'  )
    SET=$(echo "$LIST" |  head -n 1 | grep -oP '\w-\w{2}\d{2}' )
    
    
    printf "$LIST" | tee $SET.txt
    [ ! -d "img/$SET" ] && mkdir img/$SET;mv $SET.txt img/$SET; touch img/$SET/missing.txt

    python buildset.py $SET

##{{CardList/TD
##{{CardList/header/TD}}
##{{CardListV|
##{{CardList/header/V}}
}






