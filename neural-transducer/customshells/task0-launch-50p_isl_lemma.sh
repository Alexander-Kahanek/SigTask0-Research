run=bash
gpu=1


for lang in gml+50p+eng gml+50p+deu gml+50p+nno gml+75p+isl gml+25p+isl nno+50p+eng nno+50p+deu nno+50p+isl nno+75p+isl nno+25p+isl; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done