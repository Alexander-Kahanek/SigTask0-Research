#!/bin/bash
for lng in mlg ceb hil tgl mao; do
python3 example/sigmorphon2020-shared-tasks/augment.py task0-data/DEVELOPMENT-LANGUAGES/austronesian $lng --examples 10000
done
for lng in dan isl nob swe nld eng deu gmh frr ang gml nno; do
python3 example/sigmorphon2020-shared-tasks/augment.py task0-data/DEVELOPMENT-LANGUAGES/germanic $lng --examples 10000
done
for lng in nya kon lin lug sot swa zul aka gaa; do
python3 example/sigmorphon2020-shared-tasks/augment.py task0-data/DEVELOPMENT-LANGUAGES/niger-congo $lng --examples 10000
done
for lng in cpa azg xty zpv ctp czn cly otm ote pei; do
python3 example/sigmorphon2020-shared-tasks/augment.py task0-data/DEVELOPMENT-LANGUAGES/oto-manguean $lng --examples 10000
done
for lng in est fin izh krl liv vep vot mhr myv mdf sme; do
python3 example/sigmorphon2020-shared-tasks/augment.py task0-data/DEVELOPMENT-LANGUAGES/uralic $lng --examples 10000
done
