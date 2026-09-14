\read -p "Enter the source file name        : " source_file
read -p "Enter the destination file name   : " destination_file

if [ -f "$source_file" ]
then
	cp "$source_file" "$destination_file"
	echo "Content of source file $source_file is copied successfuly to the destination file $destination_file."
else
	echo "Error 404 : Source file $source_file does not exit"
fi
