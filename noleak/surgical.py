import sys
import csv
import pickle
exclude=pickle.load(open('../input/exclude.p'))

csv.field_size_limit(sys.maxsize)
name='../input/surgical_head.csv'
fea=None
dic={}
for c,row in enumerate(csv.DictReader(open(name))):
    if row['patient_id'] in exclude:
        continue
    if fea is None:
        fea={}
        for d,k in enumerate(row.keys()):
            fea[k]=d
        print fea,len(fea)
        assert(False)
    doc=' '.join(['%d_%s'%(fea[i],row[i]) for i in row if i not in ['patient_id']])
    if row['patient_id'] not in dic:
        dic[row['patient_id']]=[]
    dic[row['patient_id']].append(doc)
    if c%10000==0:
        print c

fo=open('surgical_group_train.csv','w')
fo.write('patient_id,doc\n')
name='../input/trainx.csv'
for c,row in enumerate(csv.DictReader(open(name))):
    if row['patient_id'] not in dic:
        fo.write('%s,\n'%row['patient_id'])
        continue
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(dic[row['patient_id']])))
    if c%10000==0:
        print c,'write train'
fo.close()

fo=open('surgical_group_test.csv','w')
fo.write('patient_id,doc\n')
name='../input/testx.csv'
for c,row in enumerate(csv.DictReader(open(name))):
    if row['patient_id'] not in dic:
        fo.write('%s,\n'%row['patient_id'])
        continue
    fo.write('%s,%s\n'%(row['patient_id'],' '.join(dic[row['patient_id']])))
    if c%10000==0:
        print c,'write train'
fo.close()
    #fo.write('%s,%s\n'%)
