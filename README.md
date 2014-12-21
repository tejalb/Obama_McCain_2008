Obama_McCain_2008
=================

Analyzing the 2008 Presidential campaign dataset
The dataset can be obtained from ftp://ftp.fec.gov/FEC/Presidential_Map/2008/P00000001/P00000001-ALL.zip.

1) obama_mccain.py:

Extract data for Obama and McCain from the dataset. Calculate the total amount of donations for each day and plot them to 
compare. The obtained plots show some negative donations, which we can explore further. The obtained plot is obama_mccain.png
The lines compared to negative donations look like:

C00430470   DARIEN  RETIRED McCain, John S  SA17A   P80002801   068202003       VAN MUNCHING, LEO MR. JR.   02-AUG-07   CT  X   REATTRIBUTION TO SPOUSE 315387  REATTRIBUTION TO SPOUSE -2300

C00430470   LOS ANGELES EXECUTIVE   McCain, John S  SA17A   P80002801   900492125   A.E.G.  LEIWEKE, TIMOTHY J. MR. 30-APR-08   CA  X   REFUND; REDESIGNATION REQUESTED 364146  REFUND; REDESIGNATION REQUESTED -2300

'Reattribution to Spouse' probably means that when a CEO donates to the campaign, his donation is reattributed to his spouse,
making it harder to spot which candidates are being supported by CEO's.
