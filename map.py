from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime
sys.path.append('../resources/util')
# this adds the resources/util/ folder into your python path
from map_util import *
import json

reader=csv.DictReader(open(sys.argv[1],'r'))

ob_states=defaultdict(lambda:0)
mc_states=defaultdict(int)

for row in reader:
   name=row['cand_nm']
   amount=float(row['contb_receipt_amt'])
   state_ab=row['contbr_st']
   if 'Obama' in name:
       ob_states[state_ab] += amount
   if 'McCain' in name:
       mc_states[state_ab] += amount
#dicts

max_ob = float(max(ob_states.values()))
max_mc = float(max(mc_states.values()))

print max_ob, max_mc


#for k,v in mc_states.iteritems():
#   if mc_states[item]==0:
#      print k,v

#print len(ob_states)
#print len(mc_states)

# this creates an array of grey colors from white to black
colors = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f']
colors = map(lambda s: '#%s' % (s*6), colors)
colors.sort(reverse=True)

fig=plt.figure(figsize=(40,20))

for abr,curdonation in ob_states.iteritems():
    ratio = (curdonation/max_ob)
    subplot = fig.add_subplot(121)
    subplot.set_title('Obama', fontsize='25')
    color_idx = int( ratio * (len(colors) - 1) )
    if get_statename(abr):
       state=get_statename(abr)
       draw_state(subplot, state, color=colors[color_idx])


for abr,curdonation in mc_states.iteritems():
    ratio = (curdonation/max_ob)
    subplot = fig.add_subplot(122)
    subplot.set_title('McCain',fontsize='25')
    color_idx = int( ratio * (len(colors) - 1) )
    if get_statename(abr): # Some abbreviations are corrupted
       state=get_statename(abr)
       draw_state(subplot, state, color=colors[color_idx])

# print data[:10]
#plt.legend(loc='upper center', ncol=4)
plt.savefig('map1.png', format='png')
