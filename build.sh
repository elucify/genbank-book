#!/bin/bash
set -o errexit
set -o pipefail

FORM="$1"
if [ x"$FORM" == "x" ]; then
  echo 'Usage: ./build.sh {gitbook|portal|static}'
  exit 1
fi

rm -f _layouts
ln -s layouts/$FORM _layouts

mkdir -p out

if [ "$FORM" == "gitbook" ]; then
  OUTDIR=out/gitbook
elif [ "$FORM" == "portal" ]; then
  OUTDIR=genbank
elif [ "$FORM" == static ]; then
  OUTDIR=out/static
fi

gitbook build . "out/$FORM"


if [ "$FORM" == "portal" ]; then

  # Rename all .html files -> .xml
  cd genbank
    for FILE in *.html
    do
      NAME=`echo "$FILE" | cut -d'.' -f1`
      EXT=`echo "$FILE" | cut -d'.' -f2`
      mv $FILE $NAME.xml
    done
  cd ..

fi
