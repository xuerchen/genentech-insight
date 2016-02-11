import sys
import csv
import pickle

csv.field_size_limit(sys.maxsize)
name='surgical_noleak_group_train.csv'
fo=open('surgical_noleak_code_group_train.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    tmp=[]
    for x in line:
        if x[:2]=='7_':
            claim=x[2:]
            tmp.append('%s_%s'%(claim,code))
        if x[:2]=='0_':
            code=x[2:]
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()

