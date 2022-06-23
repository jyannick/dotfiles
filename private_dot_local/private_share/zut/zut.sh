#! /bin/zsh

zut_dir=${0:a:h}
separator='µ' # single character, must not appear in the txt files

_zut() {
    grep '' -H ${zut_dir}/*.txt \
	| sed "s|${zut_dir}/||g" \
	| sed s"|.txt:|${separator}|g" \
	| sed "s| => |${separator}|g" \
    | column --table --separator ${separator} --table-columns-limit 3 \
	| fzf --height 40% \
	| awk -F"${separator}" '{print $2}'
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

