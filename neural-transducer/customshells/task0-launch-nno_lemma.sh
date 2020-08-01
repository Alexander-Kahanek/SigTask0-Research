run=bash
gpu=0


for lang in nno+25p+eng nno+25p+deu nno+75p+eng nno+75p+deu; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done