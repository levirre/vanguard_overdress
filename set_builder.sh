#set_builder.sh

read -p 'Paste Set URL Source: '  URL
echo Entered: 
echo $URL
##
LIST=$(curl $URL | grep '{{CardList/TD*' | sed 's/{{CardList*TD|//;s/..$//;s/ /_/g'  | tr '/' '-' | cut -d "|" -f 2- )
SET=$(echo "$LIST" |  head -n 1 | grep -o 'D-....' )

echo "$LIST" > $SET.txt