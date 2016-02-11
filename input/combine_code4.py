import csv
import sys
import csv
csv.field_size_limit(sys.maxsize)
D=2**30
def get(dline,pline):
    # dline: a line from diagnosis_code_group_train.csv
    # pline: a line from procedure_code_group_train.csv
    dd={} # dictionary for diagnosis code. claim_id -> diagnosis_code
    dp={} # dictionary for procedure code. claim_id -> procedure_code
    for d in dline.split():
        xx=d.split('_')
        cid=xx[0]
        dd[cid]=xx[1]
    for d in pline.split():
        xx=d.split('_')
        cid=xx[0]
        dp[cid]=xx[1]
    tmp=[]
    for d in dp:
        tmp.append(dp[d])
    return ' '.join(tmp)
diag=csv.DictReader(open('diagnosis_code_group_train.csv'))

name='procedure_code_group_train.csv'
fo=open('dp_encode4.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    pline=row['doc']
    dline=diag.next()['doc']
    nline=get(dline,pline)
    fo.write('%s,%s\n'%(row['patient_id'],nline))
    if c%10000==0:
        print c
fo.close()

diag=csv.DictReader(open('diagnosis_code_group_test.csv'))
name='procedure_code_group_test.csv'
fo=open('dp_encode_test4.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    pline=row['doc']
    dline=diag.next()['doc']
    nline=get(dline,pline)
    fo.write('%s,%s\n'%(row['patient_id'],nline))
    if c%10000==0:
        print c
fo.close()
