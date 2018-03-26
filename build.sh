#!/bin/bash
set -o errexit
set -o pipefail

FORM="${1:-static}"
if [ x"$FORM" == "x" ]; then
  echo 'Usage: ./build.sh {gitbook|portal|static}'
  exit 1
fi

rm -fr _layouts
ln -s layouts/$FORM _layouts

mkdir -p out

if [ "$FORM" == "gitbook" ]; then
  OUTDIR=out/gitbook
elif [ "$FORM" == "portal" ]; then
  OUTDIR=genbank
elif [ "$FORM" == "static" ]; then
  OUTDIR=out/static
fi

gitbook build . "$OUTDIR"


if [ "$FORM" == "portal" ]; then

  # Rename all .html files -> .xml
  CURDIR=`pwd`
  cd $OUTDIR
    for FILE in *.html
    do
      NAME=`echo "$FILE" | cut -d'.' -f1`
      EXT=`echo "$FILE" | cut -d'.' -f2`
      mv "$FILE" $NAME.xml
    done
  cd "$CURDIR"

fi
