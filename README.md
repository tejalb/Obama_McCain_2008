Obama_McCain_2008
=================

Analyzing the 2008 Presidential campaign dataset
The dataset can be obtained from ftp://ftp.fec.gov/FEC/Presidential_Map/2008/P00000001/P00000001-ALL.zip.

1) obama_mccain.py:

Extract data for Obama and McCain from the dataset. Calculate the total amount of donations for each day and plot them to compare. The obtained plots show some negative donations, which we can explore further. The obtained plot is 

![alt tag]( https://cloud.githubusercontent.com/assets/7156397/5517637/59994242-88bf-11e4-9dbe-76d9966a7965.png)

The lines corresponding to negative donations look like:

C00430470   DARIEN  RETIRED McCain, John S  SA17A   P80002801   068202003       VAN MUNCHING, LEO MR. JR.   02-AUG-07   CT  X   REATTRIBUTION TO SPOUSE 315387  REATTRIBUTION TO SPOUSE -2300

C00430470   LOS ANGELES EXECUTIVE   McCain, John S  SA17A   P80002801   900492125   A.E.G.  LEIWEKE, TIMOTHY J. MR. 30-APR-08   CA  X   REFUND; REDESIGNATION REQUESTED 364146  REFUND; REDESIGNATION REQUESTED -2300

If a donation by person A exceeds limits, then the excessive part can be "reattributed" to person B, so it appears that person B donated the rest to the campaign. 'Reattribution to Spouse' probably means that when a CEO donates to the campaign, his donation is reattributed to his spouse, making it harder to spot which candidates are being supported by CEO's.

2) obama_mccain_cumul.py

Plot the cumulative donations upto a given data, for both candidates. The plot obtained is

![alt tag](https://cloud.githubusercontent.com/assets/7156397/5517688/948f4a40-88c4-11e4-9f76-77b91b0540ac.png)


3) reattribution.py

Now to explore the REATTRIBUTION entires further, I found which field contains 'REATTRIBUTION' and found cumulative counts filtered based on this. For Obama, the entry is always 'REATTRIBUTION FROM', i.e. 'REATRIBUTION TO SPOUSE" does not appear in the entries for Obama, while for McCain this is not the case. I filtered on just the 'SPOUSE' which is contained in the memo_text field. The plot below shows cumulative donations which are reattributed.

![alt tag](https://cloud.githubusercontent.com/assets/7156397/5518048/09c91942-88e0-11e4-8dba-8b36be4a1375.png)

From a cursory glance it seems that Obama has a lot of hooded supporters. But what we really shoudl check is the ratio of the cumulative reattributed donations to the cumulative total donations, to see what fraction of the total
donations are coming from unidentified supporters.

Then the plot of this ratio looks like:

![alt tag](https://cloud.githubusercontent.com/assets/7156397/5518231/ff701ba8-88e9-11e4-977d-11b1e09a8a93.png)

This shows that a lot of McCain's donations come from CEO's, contrary to what we concluded earlier. Thus it is important to see which data is being left out before reaching conclusions, as it is easy to fabricate results that oen wants by intentionally omitting data.
