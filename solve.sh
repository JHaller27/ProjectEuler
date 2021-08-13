usage() {
    echo "Usage: $0 [-h|--help] [-d|--dry] [-u|--update] pnum"
    echo "    pnum         Problem number (eg 027)"
    echo "    -d|--dry     Dry run - show commands, but don't run them"
    echo "    -u|--update  Improve solution rather than 'solving it' for the first time"
    echo "    -p|--push    Automatically push new commit"
    echo "    -h|--help    Show this help text"
}

update=false
dry=false
pnum=-1
push=false

while [[ $# -ne 0 ]]; do
    if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
        usage
        exit
    elif [[ "$1" == "-d" ]] || [[ "$1" == "--dry" ]]; then
        dry=true
    elif [[ "$1" == "-u" ]] || [[ "$1" == "--update" ]]; then
        update=true
    elif [[ "$1" == "-p" ]] || [[ "$1" == "--push" ]]; then
        push=true
    else
        pnum="$1"
    fi

    shift
done

if [[ pnum -eq -1 ]]; then
    usage
    exit 1
fi

# git add
fname="p$pnum.py"
cmds=("git add \"$fname\"")

# git commit
if $update; then
    commit_msg="Improve"
else
    commit_msg="Solve"
fi
commit_msg="$commit_msg problem $pnum"
cmds=("${cmds[@]}", "git commit -m \"$commit_msg\"")

# git push
if $push; then
    cmds=("${cmds[@]}", "git push")
fi

for c in "${cmds[@]}"; do
    if $dry; then
        echo "$c"
    else
        "$c"
    fi
done

