
    

# $0            $1      $2
# scriptname    arg1     arg2   

echo "Name | Effect" >> effect.txt
for name in $1
do
    echo $name
    URL="https://cardfight.fandom.com/wiki/${name}?action=edit" 
#echo $URL
    eff=$(curl $URL | grep '^|effect =' | sed 's/effect = //') 
    
    echo "$name $eff" >> effect.txt
# cat ../img/D-BT01/D-BT01.txt | awk -F'|' '{print $2}'
done

# "$1" = "$(cat test.csv)"