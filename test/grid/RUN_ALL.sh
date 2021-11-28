runwithname () { echo $1 ======================================================================= | cut -c -70; python3 $1; }

runwithname test-common.py
runwithname test-source.py
runwithname test-cardinal.py
runwithname test-plane.py

echo
python3 test-1601a.py
python3 test-1602a.py
python3 test-1903a.py
python3 test-1903b.py
