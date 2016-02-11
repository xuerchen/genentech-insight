import sys
import csv
import pickle

csv.field_size_limit(sys.maxsize)

state={}
scode={}
cbsa={}
phymap={}
#diagnosis_code,diagnosis_description
name='../input/physicians.csv'
for c,row in enumerate(csv.DictReader(open(name))):
    scode[row['specialty_code']]=0
    cbsa[row['CBSA']]=0
    state[row['state']]=0
    phymap[row['practitioner_id']]='%s,%s,%s'%(row['specialty_code'],row['CBSA'],row['state'])
for c,i in enumerate(scode.keys()):
    scode[i]=c
for c,i in enumerate(cbsa.keys()):
    cbsa[i]=c+len(scode)
for c,i in enumerate(state.keys()):
    state[i]=c+len(scode)+len(state)

print 'load physicains done'


name='diagnosis_noleak_group_train.csv'
fo=open('phy_noleak_group_train.csv','w')
fo.write('patient_id,doc\n')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    count={}
    tmp=[]
    for x in line:
        if x[:2]=='0_':
            practitioner=x[2:]
            if practitioner not in phymap:
                continue
            t1,t2,t3=phymap[practitioner].split(',')
            tmp.append('1_%s'%t1)
            tmp.append('2_%s'%t2)            
            tmp.append('3_%s'%t3)

    
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()

"""
name='diagnosis_group_test.csv'
fo=open('diagnosis_phy_count_test.svm','w')
for c,row in enumerate(csv.DictReader(open(name))):
    line=row['doc'].split()
    count={}
    for x in line:
        if x[:2]=='0_':
            practitioner=x[2:]
            if practitioner not in phymap:
                continue
            t1,t2,t3=phymap[practitioner].split(',')

            if t1 in scode: 
                if scode[t1] not in count:
                    count[scode[t1]]=0
                count[scode[t1]]+=1
            if t2 in cbsa: 
                if cbsa[t2] not in count:
                    count[cbsa[t2]]=0
                count[cbsa[t2]]+=1
            if t3 in state:
                if state[t3] not in count:
                    count[state[t3]]=0
                count[state[t3]]+=1


    tmp=['%d:%d'%(code,count[code]) for code in sorted(count.keys())]
    fo.write('%s %s\n'%(row['patient_id'],' '.join(tmp)))
    if c%10000==0:
        print c
fo.close()
"""
