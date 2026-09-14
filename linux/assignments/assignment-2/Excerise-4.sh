read -p "Enter the dirctory name to create : " directory_name
i=0
mkdir "$directory_name"
echo "Success 200 : Directory created successfully."
while [ $i -lt 5 ]
do
	read -p "Enter the $i  file name to create  in the $directory_name : " file_name
	echo "welcome to unbunto linux commond for file number $i" >>  "$directory_name/$file_name"
	echo "Success 200 : file_$i file $file_name created successfully in the directroy $directory_name."
	i=$(( i + 1 ))
done

count=$(ls -l "$directory_name" | wc -l)
echo "Total numbers of file/directory inside the $directory_name is : $count" 

