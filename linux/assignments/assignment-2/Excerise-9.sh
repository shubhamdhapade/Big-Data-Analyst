TARGET_DIR="${1:-.}"
REPORT_DIR="./report"

mkdir -p "$REPORT_DIR"

file_count=$(find "$TARGET_DIR" -maxdepth 1 -type f | wc -l)

dir_count=$(find "$TARGET_DIR" -maxdepth 1 -type d | wc -l)

total_lines=$(find "$TARGET_DIR" -maxdepth 1 -type f -exec wc -l {} + 2>/dev/null | awk 'END {print $1}')

total_lines=${total_lines:-0}

cat << EOF > "$REPORT_DIR/summary.txt"
Directory Summary for : $TARGET_DIR
======================================
Files Count                     : $file_count
Directories Count               : $dir_count
Total Lines                     : $total_lines
EOF

cat "$REPORT_DIR/summary.txt"

