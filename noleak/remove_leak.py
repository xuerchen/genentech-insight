import csv
import sys
import csv
csv.field_size_limit(sys.maxsize)
D=2**30
def remove_leak(dline,pline):
    # dline: a line from diagnosis_code_group_train.csv
    # pline: a line from procedure_code_group_train.csv
    #tmp=None
    dclaim_fea={}
    pclaim_fea={}
    for c,x in enumerate(dline.split()):
        if c%6==0:
            tmp=[]
        tmp.append(x)
        if x.startswith('6_'):
            claim=x[2:]
            if claim not in dclaim_fea:
                dclaim_fea[claim]=[]
        if c%6==5:
            dclaim_fea[claim].append(' '.join(tmp))
    for c,x in enumerate(pline.split()):
        if c%16==0:
            tmp=[]
        tmp.append(x)
        if x.startswith('15_'):
            claim=x[3:]
            if claim not in pclaim_fea:
                pclaim_fea[claim]=[]
        if c%16==15:
            pclaim_fea[claim].append(' '.join(tmp))
    ndline,npline=[],[]
    for claim in dclaim_fea:
        if claim in pclaim_fea:
            ndline=ndline + dclaim_fea[claim]
            npline=npline + pclaim_fea[claim]
    ndline=' '.join(ndline)
    npline=' '.join(npline)
    return ndline,npline
    


diag=csv.DictReader(open('../input/diagnosis_group_train.csv'))

name='../input/procedure_group_train.csv'
fo1=open('diagnosis_noleak_group_train.csv','w')
fo1.write('patient_id,doc\n')
fo2=open('procedure_noleak_group_train.csv','w')
fo2.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    pline=row['doc']
    dline=diag.next()['doc']
    #assert(len(pline.split())%16==0)
    #assert(len(dline.split())%6==0)
    #print len(pline.split())%16,len(dline.split())%6#,len(pline.split())%17
    ndline,npline=remove_leak(dline,pline)
    fo1.write('%s,%s\n'%(row['patient_id'],ndline))
    fo2.write('%s,%s\n'%(row['patient_id'],npline))
    if c%10000==0:
        print c,len(dline),len(ndline),len(pline),len(npline)

fo1.close()

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
