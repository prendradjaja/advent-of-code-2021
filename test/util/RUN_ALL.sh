runwithname () { echo $1 ======================================================================= | cut -c -70; python3 $1; }

runwithname test-util.py
echo
python3 -m doctest util.py && echo OK util.py doctests
