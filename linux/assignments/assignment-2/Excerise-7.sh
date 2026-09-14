awk -F',' '$3 >= 80 {print $1 ", " $3 }' students.csv
