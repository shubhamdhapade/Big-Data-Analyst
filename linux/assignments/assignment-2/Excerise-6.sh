cut -d',' -f2 students.csv | sort | uniq -c | tr -s ' ' | awk '{print $2 " : " $1 }'
#lower case
cut -d',' -f2 students.csv | tr '[:upper:]' '[:lower:]' | sort | uniq -c | tr -s ' ' | sed 's/^ //'
#
cut -d',' -f2 students.csv | sed '/^[[:space:]]*$/d' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | tr -s ' ' | sed 's/^ //'

