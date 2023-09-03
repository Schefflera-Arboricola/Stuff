#!/bin/bash

if ! [ -f ~/se2001/assignment_9/script.sh ]; then
    echo "File $HOME/se2001/assignment_9/script.sh not found" >&2
    exit 1
fi

if ! [ -x ~/se2001/assignment_9/script.sh ]; then
    echo "File $HOME/se2001/assignment_9/script.sh is not executable" >&2
    exit 1
fi

classes=("setosa" "versicolor" "virginica")
features=("sepal_length" "sepal_width" "petal_length" "petal_width")

in="/opt/se2001/assignment_9/info.txt"

ni=(1 3 5)
fi=(1 2 3 4)

nc="${#classes[@]}"
nf="${#features[@]}"

for i in {1..5}; do
    c=`shuf -i 0-$(( $nc-1 )) -n 1`
    f=`shuf -i 0-$(( $nf-1 )) -n 1`

    class="${classes[c]}"
    feature="${features[f]}"

    j="${ni[c]}"
    l="${fi[f]}"
    
    x=$( sed -ne "$j"p "${in}" | sed "s/[ ]\+/ /g" | cut -d " " -f "$l" )
    js=`./script.sh "$class" "$feature"`

    if [ -z "$js" ]; then
	echo Invalid output from script.sh >&2
        exit 1;
    fi
    
    ce="Iris-${class}"
    fe=${feature}

    ca=`echo ${js} | jq -r ".class"`
    fa=`echo ${js} | jq -r ".feature"`
    ma=`echo ${js} | jq ".mean"`
    
    mf=`echo "${ma} == ${x}" | bc`

    if [ "${mf}" -eq 0 ]; then
	echo Invalid mean
        exit 1
    fi
    if [ "${ca}" != "${ce}" ]; then
	echo Invalid class Expected: "$ce" Actual: "$ca" 
        exit 1
    fi
    if [ "${fa}" != "${fe}" ]; then
	echo Invalid feature  Expected: "$fe" Actual: "$fa"
        exit 1
    fi
done
