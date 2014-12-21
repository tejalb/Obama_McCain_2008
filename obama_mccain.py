from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime

reader=csv.DictReader(open(sys.argv[1],'r'))

obamadonations=defaultdict(lambda:0)
mccaindonations=defaultdict(int)

for row in reader:
    name=row['cand_nm']
    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
    date=datetime.datetime.strptime(datestr, '%d-%b-%y')
#    if amount<0:
#        print row.values()
#        str1=''.join(row.values())
#        line='\t'.join(str1)
#        print line
    if 'Obama' in name:
        obamadonations[date] += amount
    if 'McCain' in name:
        mccaindonations[date] += amount
# dicts

sort_by_date_o= sorted(obamadonations.items(), key=lambda (key,val): key)
sort_by_date_m= sorted(mccaindonations.items(), key=lambda (key,val): key)
xo,yo=zip(*sort_by_date_o)
xm,ym=zip(*sort_by_date_m)
plt.plot(xo,yo,label=' Obama\'s donations')
plt.plot(xm,ym,label=' McCain\'s donations')
plt.legend(loc='upper center', ncol=4)
plt.savefig('obama_mccain.png', format='png')
