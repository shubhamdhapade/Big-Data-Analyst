DATA_DIR='./data'
BACKUP_DIR='./backup'

if [ -d "$DATA_DIR" ]
then
	mkdir -p "$BACKUP_DIR"
	if compgen -G "$DATA_DIR/*.txt" > /dev/null; then
		cp "$DATA_DIR"/*.txt "$BACKUP_DIR"/
		echo "Bcakup completed successfully."
	else
		echo "No .txt file found in the $DATA_DIR directory."
	fi
else
	echo "Error 404 : No $DATA_DIR directory found"
fi
