read -p "Enter the directory name : " directory_name

if [ -d "$directory_name" ]
then

	echo "Success 200 : Directory $directory_name found with the below details "
	ls "$directory_name"  #it will show the details of current directory 
else
	echo "Error 404 :Directory does not exit, we are creating the directory with demo.py file only."
	mkdir "$directory_name" #it will create the directory in the current directory.
	touch "$directory_name/demo.py"
fi
