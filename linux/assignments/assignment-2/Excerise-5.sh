read -p "Enter the name of directory : " directory_name
read -p "Enter the name of extension : " extension_name

if [ -d "$directory_name" ]
then
        count=$(find "$directory_name" -type f -name "*.$extension_name" | wc -l)

        if [ $count -gt 0 ]
        then
                find "$directory_name" -type f -name "*.$extension_name"
                echo "Number of files in the $directory_name directory for .$extension_name is : $count"
        else
                echo "No .$extension_name files found in $directory_name directory."
        fi
else
        echo "Error 404: Directory does not exist."
fi

