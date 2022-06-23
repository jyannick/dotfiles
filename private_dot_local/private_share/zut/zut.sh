#! /bin/zsh

zut_dir=${0:a:h}
intermediary_separator='µ' # single character, must not appear in the txt files
display_separator='   |   ' # can be multiple characters, must look fine on screen
display_splitter='|' # single character contained in display_separator

_zut() {
    grep '' -H ${zut_dir}/*.txt \
	| sed "s|${zut_dir}/||g" \
	| sed s"|.txt:|${intermediary_separator}|g" \
	| sed "s| => |${intermediary_separator}|g" \
	| column --table --separator ${intermediary_separator} --output-separator ${display_separator} \
	| fzf --height 40% \
	| awk -F"${display_splitter}" '{gsub(/[ \t]+$/, "", $2); gsub(/^[ \t]+/, "", $2); print $2}'
}

zut() {
    print -z $(_zut)

}

_zut_widget() {
    zle kill-whole-line
    zle -U "$(_zut)"
    zle accept-line
}

zle -N _zut_widget
bindkey "^H" _zut_widget

