#!/bin/bash
fibonacci() {
    n=$1
    x0=0
    x1=1
    if [[ $n -lt 0 ]]; then
        exit 1
    elif [[ $n = 0 ]]; then
        echo $x0
    elif [[ $n = 1 ]]; then
        echo $x1
    else
        for ((i = 2 ; i <= $n ; i++)); do 
            x=$((x0+x1))
            x0=$x1
            x1=$x
        done
        echo $x1
    fi
}
