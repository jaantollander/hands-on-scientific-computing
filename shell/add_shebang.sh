#!/bin/bash

SHEBANG="#!/bin/bash"
for FILE in $*; do
    # Skip files that already have shebang, that is, starts with "#!".
    HEAD=`head $FILE -n 1`
    if [[ ! ${HEAD:0:2} = "#!" ]]; then
        CONTENTS=`cat $FILE`
        echo $SHEBANG > $FILE
        echo $CONTENTS >> $FILE
    fi
done
