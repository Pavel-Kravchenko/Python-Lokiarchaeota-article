
# coding: utf-8

# In[96]:


import re
from Bio import AlignIO

b = open('36_positions.txt')
posit = list(map(lambda x: x.split(), b.readlines()))[:-1]
coord1 = list((i[0].split('->')[0] for i in posit))
coord2 = list((i[0].split('->')[1] for i in posit))
names = list((i[1] for i in posit))
b.close()

alignment = AlignIO.read("36.phy", "phylip-relaxed")
for i in range(len(names)):
    AlignIO.write(alignment[:, (int(coord1[i])-1):(int(coord2[i]))], names[i]+".phy", "phylip-relaxed")

