#!/bin/bash

set -e

if [[ $# == 0 ]] ; then
    echo "Must provide a tag (eg. 1.2)"
    exit 1
fi

docker build -t bbb:$1 .
