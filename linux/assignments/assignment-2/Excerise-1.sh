read -p "Enter the file name : " file_name

if [ -f "$file_name" ]
then
	#it is give the all details of file with size
#	ls -lh "$file_name"
	#it will give exact the file size without any other content
#	stat -c %s "$file_name"
	#it will five the size in kb with filename
#	du -sh "$file_name"
	
	size=$(stat -c %s "$file_name")
	echo "$file_name File size is : $size bytes." 

	lines=$(wc -l < "$file_name")
	echo "Number of line/(s) in the $file_name file is : $lines line/(s). "

	words=$(wc -w < "$file_name")
	echo "Number of word/(s) in the $file_name file is : $words word/(s). "

	characters=$(wc -m < "$file_name")
	echo "Number of character/(s) in the $file_name is : $characters character/(s). "
else
	echo "File does not exit, kindly first make the file and then check"
fi
