import csv
import pickle
fea=pickle.load(open('fea.p'))
reader9=csv.DictReader(open('features/fea9.csv'))
reader10=csv.DictReader(open('features/fea10.csv'))
reader11=csv.DictReader(open('features/fea11.csv'))
fo=open('features/allfeatures.csv','w')
fo.write('patient_id,is_screener,%s\n'%(','.join(fea)))
for c,row in enumerate(csv.DictReader(open('features/fea12.csv'))):
    tmp=[i[2:] for i in row['features'].split()]
    tmp+=[i[2:] for i in reader11.next()['features'].split()]
    tmp+=reader9.next()['features'].split()
    tmp+=reader10.next()['features'].split()
    count={}
    for i in fea:
        count[i]=0
    for i in tmp:
        if i in count:
            count[i]+=1
    tmp=[str(count[i]) for i in fea]
    fo.write('%s,%s,%s\n'%(row['patient_id'],row['is_screener'],','.join(tmp)))
    if c%100000==0:
        print c,
fo.close()
