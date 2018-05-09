echo "/Bash script run successfully/"

a=*.phy
for x in $a
do
 mkdir ${x%.phy}
 cd ${x%.phy} 
 cp ../$x .
 echo "/Drawing trees/"
 phyml -i $a -d aa --no_memory_check
 fdrawgram -intreefile *tree -plotfile tree.c.fdrawgram -auto -style c -previewer n
 echo "/Done/"
 cd ..
done
echo "/Bash script end successfully/"

