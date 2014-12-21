from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime
import numpy as np

reader=csv.DictReader(open(sys.argv[1],'r'))

obamadonations=[]
mccaindonations=[]

for row in reader:
    name=row['cand_nm']
#    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
#    date=datetime.datetime.strptime(datestr, '%d-%b-%y')
#    if amount<0:
#        print row.values()
#        str1=''.join(row.values())
#        line='\t'.join(str1)
#        print line
    if 'Obama' in name:
        obamadonations.append(amount)
    if 'McCain' in name:
        mccaindonations.append(amount)
# dicts

print len(obamadonations)


plt.hist(obamadonations,label=' Obama\'s donations',alpha=0.5,color='yellow',edgecolor="none",bins=range(-18000,19000,100))
plt.hist(mccaindonations,label=' McCain\'s donations',alpha=0.5,color='red',edgecolor="none",bins=range(-22000,23000,100))
 
plt.legend(loc='upper left', ncol=1)
plt.savefig('ob_mc_hist.png', format='png')
