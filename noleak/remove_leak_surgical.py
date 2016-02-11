import csv
import sys
import csv
csv.field_size_limit(sys.maxsize)
D=2**30
def remove_leak(dline,sline):
    if sline=='':
        return sline
    sclaim_fea={}
    dclaim_fea={}
    for c,x in enumerate(dline.split()):
        if x.startswith('6_'):
            claim=x[2:]
            if claim not in dclaim_fea:
                dclaim_fea[claim]=1
    for c,x in enumerate(sline.split()):
        if c%9==0:
            tmp=[]
        tmp.append(x)
        if x.startswith('7_'):
            claim=x[2:]
            if claim not in sclaim_fea and claim in dclaim_fea:
                sclaim_fea[claim]=[]
        if c%9==8:
            if claim in sclaim_fea:
                sclaim_fea[claim].append(' '.join(tmp))
    nsline=[]
    for claim in sclaim_fea:
        nsline=nsline + sclaim_fea[claim]
    nsline=' '.join(nsline)
    return nsline
    


diag=csv.DictReader(open('diagnosis_noleak_group_train.csv'))

name='../input/surgical_group_train.csv'
fo2=open('surgical_noleak_group_train.csv','w')
fo2.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    sline=row['doc']
    dline=diag.next()['doc']
    nsline=remove_leak(dline,sline)
    fo2.write('%s,%s\n'%(row['patient_id'],nsline))
    if c%10000==0:
        print c,len(sline),len(nsline)#,len(pline),len(npline)

fo2.close()

"""
diag=csv.DictReader(open('diagnosis_group_test.csv'))
name='procedure_group_test.csv'
fo1=open('diagnosis_noleak_group_test.csv','w')
fo1.write('patient_id,doc\n')
fo2=open('procedure_noleak_group_test.csv','w')
fo2.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    pline=row['doc']
    dline=diag.next()['doc']
    nline=remove_leak(dline,pline)
    fo.write('%s,%s\n'%(row['patient_id'],nline))
    if c%10000==0:
        print c
fo.close()
"""
