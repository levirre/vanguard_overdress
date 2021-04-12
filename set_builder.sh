#set_builder.sh

echo ------Paste Set URL Source-----------
read URL
echo Entered: 
echo "$URL"

# 
curl $URL | grep '{{CardList/TD*' | sed 's/{{CardList*TD|//;s/..$//;s/ /_/g'  | tr '/' '-' | cut -d "|" -f 2-