#this part preprocesses data with leak features
cd ../input/
pypy exclude.py
pypy diag.py
pypy procedure.py
pypy getcode.py
pypy combine_code1.py
pypy combine_code3.py 
pypy combine_code4.py

#extract features with leak
cd ../online2
mkdir features predictions
pypy select8.py

#remove leak and re-preprocess the data
cd ../noleak
pypy remove_leak.py
pypy getcode.py
pypy remove_leak_surgical.py
pypy remove_leak_physician.py
pypy getcode_surgical.py
pypy combine_code1.py
pypy combine_code3.py
pypy combine_code4.py
pypy combine_code5.py
pypy combine_code6.py

#extract features without leak
cd ../online2
pypy select9.py
pypy select10.py
pypy select11.py
pypy select12.py



 
