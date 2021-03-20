#!/bin/sh

wget https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.1/montreal-forced-aligner_linux.tar.gz

tar -xzf montreal-forced-aligner_linux.tar.gz

mkdir out
mkdir aligner

git clone https://github.com/nbusser/SM-Dictionaries.git

wget https://github.com/MontrealCorpusTools/mfa-models/raw/master/acoustic/french_prosodylab.zip

echo "mfa align \$@" > align.sh
chmod +x align.sh

echo "
{
    \"align_exe\": \"./align.sh\",
    \"trained_model\": \"aligner/pretrained_models/french_prosodylab.zip\",
    \"dict_path\": \"aligner/fr.dict\",
    \"dict_consonant_vowel_path\": \"aligner/fr_consonant_vowel.dict\",
    \"lang\": \"fr\",
    \"folder\": \".subs\"
}" > config.json


pyinstaller --name="P00pMaker" --windowed ../video_creator_main.py --add-data aligner:aligner --add-data out:aligner/out --add-data SM-Dictionaries/fr.dict:aligner --add-data SM-Dictionaries/fr_consonant_vowel.dict:aligner --add-data french_prosodylab.zip:aligner/pretrained_models --add-data config.json:. --add-data align.sh:.

rm montreal-forced-aligner_linux.tar.gz
rm french_prosodylab.zip
rm -rf montreal-forced-aligner
rm -rf out aligner
rm -rf SM-Dictionaries
rm config.json
rm align.sh
