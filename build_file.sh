echo " BUILD START"
python3.9 -m pip install -r requirement.txt
python3.9 manage.py colllectstatic --noinput --clear
echo " BUILD END"