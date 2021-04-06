#!/bin/sh

PARAM=$1

rm -rf build
rm -rf dist
rm *.spec

source "./.variables.sh"

if [ "${PARAM}" = "--hard" ]; then
    rm "${ARCHIVE_NAME}"
    rm "${MFA_ARCHIVE_NAME}"
    rm "${FRENCH_MODEL_NAME}"
fi
