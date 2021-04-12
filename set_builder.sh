#set_builder.sh

read -p 'Paste Set URL Source: '  URL
echo Entered: 
echo $URL
##
LIST=$(curl $URL | grep '{{CardList*' | grep -v 'header\|footer'| sed 's/..$//;s/ /_/g' | cut -d "|" -f 2- | tr '/' '-'  )
SET=$(echo "$LIST" |  head -n 1 | grep -o '.-....' )

printf "$LIST" 

##{{CardList/TD
##{{CardList/header/TD}}
##{{CardListV|
##{{CardList/header/V}}


