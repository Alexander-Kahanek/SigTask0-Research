run=bash
# aka ang azg ceb cly cpa ctp czn dan deu eng est fin ----- running on gpu 0
for lang in zul zpv xty vot vep tgl swe swa sot sme pei otm ote nya nob nld myv mlg mhr mdf mao lug liv lin krl kon izh isl hil gmh gaa frr ; do
# regular data
echo trm $lang
$run example/sigmorphon2020-shared-tasks/0task0-trm.sh $lang
echo mono $lang
$run example/sigmorphon2020-shared-tasks/0task0-mono.sh $lang

# augmented data
echo trm hall $lang
$run example/sigmorphon2020-shared-tasks/0task0-hall-trm.sh $lang
echo mono hall $lang
$run example/sigmorphon2020-shared-tasks/0task0-hall-mono.sh $lang
done
    
for lang in uralic oto-manguean niger-congo germanic austronesian; do
# regular data
echo trm $lang
$run example/sigmorphon2020-shared-tasks/0task0-trm.sh $lang
echo mono $lang
$run example/sigmorphon2020-shared-tasks/0task0-mono.sh $lang

# augmented data
echo trm hall $lang
$run example/sigmorphon2020-shared-tasks/0task0-hall-trm.sh $lang
echo mono hall $lang
$run example/sigmorphon2020-shared-tasks/0task0-hall-mono.sh $lang
done