FILES=*/*.rst
for f in $FILES
do
  filename="${f%.*}"
  echo "rename $f to $filename.md"
  `mv $f $filename.md`
done
