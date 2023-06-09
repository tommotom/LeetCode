#!/usr/bin/env bash
clear
echo -n "INPUT_DATE(YYYYMMDD):"
read -r str

YYYY=${str:0:4}
MM=${str:4:2}
DD=${str:6:2}

[ ! -d "$YYYY" ] && mkdir "$YYYY"
[ ! -d "$YYYY/$MM" ] && mkdir "$YYYY/$MM"
[ ! -d "$YYYY/$MM/$DD" ] && mkdir "$YYYY/$MM/$DD"

touch "$YYYY"/"$MM"/"$DD"/Solution.tsx
