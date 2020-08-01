run=bash
gpu=1


for lang in gml+25p+eng gml+25p+deu gml+25p+nno gml+75p+eng gml+75p+deu gml+75p+nno; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done