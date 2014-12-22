Obama_McCain_2008
=================

Analyzing the 2008 Presidential campaign dataset
The dataset can be obtained from ftp://ftp.fec.gov/FEC/Presidential_Map/2008/P00000001/P00000001-ALL.zip.
This is a large dataset containing ** 4085666 ** lines.

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

Now to explore the REATTRIBUTION entires further, I found which field contains 'REATTRIBUTION' and found cumulative counts filtered based on this. For Obama, the entry is always 'REATTRIBUTION FROM', i.e. 'SPOUSE' does not appear in the entries for Obama, while for McCain this is not the case. I filtered on just 'REATTRIBUTION FROM' which is contained in the memo_text field. The plot below shows cumulative donations which are reattributed.

![alt tag] (https://cloud.githubusercontent.com/assets/7156397/5518262/462eb052-88ec-11e4-9166-a68f866450b2.png)

From a cursory glance it seems that Obama has a lot of hooded supporters. But what we really shoudl check is the ratio of the cumulative reattributed donations to the cumulative total donations, to see what fraction of the total
donations are coming from unidentified supporters.

4) reattribution_ratio.py

Then the plot of all cumulative donations, both reattributed as well as total, looks like this:

![alt tag](https://cloud.githubusercontent.com/assets/7156397/5518583/d3e096e4-88fc-11e4-9892-15b6def6afa4.png)

This shows that a lot of McCain's donations come from CEO's, contrary to what we concluded earlier. Thus it is important to see which data is being left out before reaching conclusions, as it is easy to fabricate results that oen wants by intentionally omitting data.

5) hist.py

Here is a histogram of donations with a binwidth of $100. Since the range of donations is very large, varying from -$1 million to $8 million, while majority of donations are less than 2000, we only display bins from -$22000 to $22000.

![alt tag](https://cloud.githubusercontent.com/assets/7156397/5519103/bee0cfa6-8911-11e4-8866-f90915a98c66.png)

