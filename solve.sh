usage() {
    echo "Usage: $0 [-h|--help] [-d|--dry] [-u|--update] pnum"
    echo "    pnum         Problem number (eg 027)"
    echo "    -d|--dry     Dry run - show commands, but don't run them"
    echo "    -u|--update  Improve solution rather than 'solving it' for the first time"
    echo "    -h|--help    Show this help text"
}

update=false
dry=false
pnum=-1

while [[ $# -ne 0 ]]; do
    if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
        usage
        exit
    elif [[ "$1" == "-d" ]] || [[ "$1" == "--dry" ]]; then
        dry=true
    elif [[ "$1" == "-u" ]] || [[ "$1" == "--update" ]]; then
        update=true
    else
        pnum="$1"
    fi

    shift
done

if [[ pnum -eq -1 ]]; then
    usage
    exit 1
fi

if $update; then
    commit_msg="Improve"
else
    commit_msg="Solve"
fi
commit_msg="$commit_msg problem $pnum"

fname="p$pnum.py"

if $dry; then
    echo "git add \"$fname\""
    echo "git commit -m \"$commit_msg\""
else
    git add $fname
    git commit -m "$commit_msg"
fi

