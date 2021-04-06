#!/bin/sh

source "./.variables.sh"

if [ ! -f "${MFA_ARCHIVE_NAME}" ]; then
    wget "${MFA_LINK}"
fi
tar -xzf montreal-forced-aligner_linux.tar.gz

if [ ! -f "${FRENCH_MODEL_NAME}" ]; then
    wget "${MODEL_LINK}"
fi

git clone https://github.com/nbusser/SM-Dictionaries.git

mkdir out

echo "
{
    \"align_exe\": \"aligner/bin/mfa_align\",
    \"trained_model\": \"aligner/pretrained_models/${FRENCH_MODEL_NAME}\",
    \"dict_path\": \"aligner/SM-Dictionaries/fr/fr.dict\",
    \"dict_consonant_vowel_path\": \"aligner/SM-Dictionaries/fr/fr_consonant_vowel.dict\",
    \"lang\": \"fr\",
    \"folder\": \".subs\"
}" > config.json

pyinstaller --name="${PROJECT_NAME}" ../video_creator_main.py --add-data montreal-forced-aligner/bin:aligner/bin --add-data montreal-forced-aligner/pretrained_models:aligner/pretrained_models --add-data montreal-forced-aligner/lib:aligner/bin --add-data out:aligner/out --add-data SM-Dictionaries:aligner/SM-Dictionaries --add-data french_prosodylab.zip:aligner/pretrained_models --add-data config.json:.

rm dist/SentenceMixerCLI/aligner/pretrained_models/english.zip

cp -r dist/"${PROJECT_NAME}" .
tar -czvf "${ARCHIVE_NAME}" "${PROJECT_NAME}"
rm -rf "${PROJECT_NAME}"

rm -rf montreal-forced-aligner
rm -rf out
rm -rf SM-Dictionaries
rm config.json
