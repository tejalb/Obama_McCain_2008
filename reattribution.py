from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime

reader=csv.DictReader(open(sys.argv[1],'r'))

obamadonations=defaultdict(lambda:0)
mccaindonations=defaultdict(int)
obamatot=defaultdict(int)
mccaintot=defaultdict(int)

for row in reader:
    name=row['cand_nm']
    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
    date=datetime.datetime.strptime(datestr, '%d-%b-%y')
#    for k,v in row.items():
#        if 'TO SPOUSE' in v:
#            print k,v
#            break;
    if 'Obama' in name:
        obamatot[date] += amount
    if 'McCain' in name:
        mccaintot[date] += amount

    if 'REATTRIBUTION' in row['receipt_desc']:
#        print amount
#        print name
        if 'Obama' in name:
           obamadonations[date] += amount
#           print obamadonations[date]
        elif 'McCain' in name and 'FROM SPOUSE' in row['receipt_desc']:
            mccaindonations[date] += amount
#            print mccaindonations[date]
# dicts


sort_by_date_o= sorted(obamadonations.items(), key=lambda (key,val): key)
sort_by_date_m= sorted(mccaindonations.items(), key=lambda (key,val): key)
xo,yo=zip(*sort_by_date_o)
xm,ym=zip(*sort_by_date_m)

yo_cl=[]
ym_cl=[]
cumul=0
for num in yo:
    cumul+=num
    yo_cl.append(cumul)

cumul=0
for num in ym:
    cumul+=num
    ym_cl.append(cumul)

plt.plot(xo,yo_cl,label=' Obama\'s donations')
plt.plot(xm,ym_cl,label=' McCain\'s donations')
plt.legend(loc='upper center', ncol=4)
plt.savefig('spouse.png', format='png')
