source_dir="$1"
target_dir="$2"

for source_file in $source_dir/*.ui
do	
	target_file=${source_file#"$source_dir"}
	target_file=${target_file%".ui"}

	target_file="$target_dir$target_file.py"

	pyuic5 -x "$source_file" -o $target_file
done
