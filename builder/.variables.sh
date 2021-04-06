#!/bin/sh

PROJECT_NAME="SentenceMixerCLI"
ARCHIVE_NAME="${PROJECT_NAME}".tar.gz

MFA_LINK="https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.1.0-beta.2/montreal-forced-aligner_linux.tar.gz"
MFA_ARCHIVE_NAME=$(basename "${MFA_LINK}")

MODEL_LINK="https://github.com/MontrealCorpusTools/mfa-models/raw/master/acoustic/french_prosodylab.zip"
FRENCH_MODEL_NAME=$(basename "${MODEL_LINK}")
