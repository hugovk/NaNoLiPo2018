# Usage: moo.sh infile.txt "Title of PDF"

echo $1 $2
wc -w $1

python3 moo.py $1 > moo-$1
wc -w moo-$1

python3 moo.py -t $1 > moo-x2-$1
wc -w moo-x2-$1

echo "PDF:" moo-$1
# https://openbookproject.googlecode.com/svn/tangle/html2pdf/reportlab_2_1/reportlab/tools/py2pdf/py2pdf.py
# pip install reportlab
py2pdf.py --fontSize 10 --mode mono --title "$2" moo-$1

echo "PDF:" moo-x2-$1
# http://two.pairlist.net/pipermail/reportlab-users/2007-February/005791.html
# http://two.pairlist.net/pipermail/reportlab-users/attachments/20070213/80c61e82/attachment.obj
txt2pdf.py moo-x2-$1
