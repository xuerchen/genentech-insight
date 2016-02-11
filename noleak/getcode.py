import sys
import csv
import pickle

csv.field_size_limit(sys.maxsize)
name='diagnosis_noleak_group_train.csv'
fo=open('diagnosis_noleak_code_group_train.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    tmp=[]
    for x in line:
        if x[:2]=='6_':
            claim=x[2:]
            tmp.append('%s_%s'%(claim,code))
        if x[:2]=='2_':
            code=x[2:]
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()
"""
name='diagnosis_noleak_group_test.csv'
fo=open('diagnosis_noleak_code_group_test.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    tmp=[]
    for x in line:
        if x[:2]=='6_':
            claim=x[2:]
            tmp.append('%s_%s'%(claim,code))
        if x[:2]=='2_':
            code=x[2:]
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()
"""
name='procedure_noleak_group_train.csv'
fo=open('procedure_noleak_code_group_train.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    tmp=[]
    for x in line:
        if x.startswith('15_'):
            claim=x[3:]
        if x.startswith('16_'):
            code=x[3:]
            tmp.append('%s_%s'%(claim,code))
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()
"""
name='procedure_noleak_group_test.csv'
fo=open('procedure_noleak_code_group_test.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    tmp=[]
    for x in line:
        if x.startswith('15_'):
            claim=x[3:]
        if x.startswith('16_'):
            code=x[3:]
            tmp.append('%s_%s'%(claim,code))
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()
"""
