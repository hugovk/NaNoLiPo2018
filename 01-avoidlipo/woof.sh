# Usage: woof.sh infile.txt "Title of PDF"

echo $1 $2
wc -w $1

python3 woof.py $1 > woof-$1
wc -w woof-$1

python3 woof.py -t $1 > woof-x2-$1
wc -w woof-x2-$1

echo "PDF:" woof-$1
# https://openbookproject.googlecode.com/svn/tangle/html2pdf/reportlab_2_1/reportlab/tools/py2pdf/py2pdf.py
# pip install reportlab
py2pdf.py --fontSize 10 --mode mono --title "$2" woof-$1

echo "PDF:" woof-x2-$1
# http://two.pairlist.net/pipermail/reportlab-users/2007-February/005791.html
# http://two.pairlist.net/pipermail/reportlab-users/attachments/20070213/80c61e82/attachment.obj
txt2pdf.py woof-x2-$1
