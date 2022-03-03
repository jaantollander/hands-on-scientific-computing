#!/bin/bash
get_basename() {
    STR=$1
    BASEPATH=${STR##*/}
    echo ${BASEPATH%%.*}
}

get_extension() {
    STR=$1
    BASEPATH=${STR##*/}
    # FIXME: if no extension /user/name
    EXT=${BASEPATH##*.}
    if [[ $EXT = $BASEPATH ]]; then
        echo ""
    else
        echo $EXT
    fi
}
