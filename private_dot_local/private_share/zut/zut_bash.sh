#! /bin/bash

zut_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
intermediary_separator='µ' # single character, must not appear in the txt files
display_separator='   |   ' # can be multiple characters, must look fine on screen
display_splitter='|' # single character contained in display_separator

zut () {
    grep '' -H ${zut_dir}/*.txt \
	| sed "s;${zut_dir}/;;g" \
	| sed s";.txt:;${intermediary_separator}${display_separator};g" \
	| sed "s; => ;${intermediary_separator}${display_separator};g" \
	| column -t -s ${intermediary_separator}\
	| fzf --height 40% \
	| awk -F"${display_splitter}" '{gsub(/[ \t]+$/, "", $2); gsub(/^[ \t]+/, "", $2); print $2}' \
	| awk '{print "❯ " $0; system($0)}'
}

bind '"\C-h":"zut\n"'
