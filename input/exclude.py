import csv
import pickle
exclude={}
f=open('train_patients_to_exclude.csv')
for line in f:
    exclude[line.strip()]=1
f.close()
f=open('test_patients_to_exclude.csv')
for line in f:
    exclude[line.strip()]=1
f.close()
print 'exclude done'
pickle.dump(exclude,open('exclude.p','w'))
name='patients_train.csv'
f=open(name)
fo=open('trainx.csv','w')
fo.write(f.readline())
for c,row in enumerate(csv.DictReader(open(name))):
    line=f.readline()
    if row['patient_id'] in exclude:
        continue
    fo.write(line)
fo.close()
fo.close()
print 'write train done'

name='patients_test.csv'
f=open(name)
fo=open('testx.csv','w')
fo.write(f.readline())
for c,row in enumerate(csv.DictReader(open(name))):
    line=f.readline()
    if row['patient_id'] in exclude:
        continue
    fo.write(line)
fo.close()
fo.close()
print 'write test done'
