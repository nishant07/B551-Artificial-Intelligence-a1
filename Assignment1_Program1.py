
"""
Problem Statement:
 The customer who ordered the Candelabrum received the
Banister, while the customer who ordered the Banister received the package that Irene had ordered.
Frank  received  a  Doorknob.   George's  package  went  to  Kirkwood  Street.   The  delivery  that  should
have gone to Kirkwood Street was sent to Lake Avenue.  Heather received the package that was to go
to Orange Drive.  Jerry received Heather's order.  The Elephant arrived in North Avenue; the person
who had ordered it received the package that should have gone to Maxwell Street.  The customer on
Maxwell Street received the Amplifier. 
"""
"""
Solution:
We took a dictonary with keys are arrival/received location of the item and their values are list of who ordered that item and where actually it should have received.
We initialized these list with all posssible values.
We kept removing the items from these list as per the information given.
After removing as far as posssible, we left with 6 other fact. We checked  which remaining possibilities hold for these 6 condition/facts.
And we arivided at only 1 solution.
"""
rec_loc = {'K':[['a','b','c','d','e'],['f','g','h','i','j'],['l','m','n','o']],
'L':[['a','b','c','d','e'],['f','g','h','i','j'],['k','m','n','o']],
'M':[['a','b','c','d','e'],['f','g','h','i','j'],['k','l','n','o']],
'N':[['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','o']],
'O':[['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n']]}

itm_map = {'a':'Amplifier', 'b':'Banister','c':'Candelabrum','d':'Doorknob','e':'Elephant'}
per_map = {'f':'Frank','g':'George','h':'Heather', 'i':'Irene','j':'Jerry'}
loc_map = {'k':'Kirkwood Street','l':'Lake Avenue','m':'Maxwell Street','n':'North Avenue','o':'Orange Drive'}
#The  delivery  that  should have gone to Kirkwood Street was sent to Lake Avenue.
rec_loc['L'][2]=['k']
#The Elephant arrived in North Avenue; 
#the person who had ordered it received the package that should have gone to Maxwell Street.   
rec_loc['N'][0] = ['e']
rec_loc['N'][2].remove('m')
#The customer on Maxwell Street received the Amplifier.
rec_loc['M'][0] = ['a']
#George's  package  went  to  Kirkwood  Street.   
rec_loc['K'][1] = ['g']

try:
	for i, j in rec_loc.items():
		if (i != 'L' and 'k' in j[2]):
			j[2].remove('k')
		if (i != 'N' and 'e' in j[0]):
			j[0].remove('e')
		if (i != 'M' and 'a' in j[0]):
			j[0].remove('a')
		if (i != 'K' and 'g' in j[1]):
			j[1].remove('g')		
except ValueError:
	print 'Wrong logic'
	raise

#Frank  received  a  Doorknob. 
"""
item('d') != person('f')
rec_loc() of item 'd' = loc() of person 'f'  
"""
#Heather received the package that was to go to Orange Drive.
"""
person('h') != loc('o')
rec_loc() of location 'o'= loc() of person 'h' 
"""

#Jerry received Heather's order. 
"""
rec_loc() of person 'h' = loc() of person 'j'  
"""

#The Elephant arrived in North Avenue;  the person who had ordered it received the package that should have gone to Maxwell Street.
"""
loc() of item 'e' = rec_loc() of location 'm'
"""

#The customer who ordered the Candelabrum received the Banister, while the customer who ordered the Banister received the package that Irene had ordered. 
"""
rec_loc() of item 'b' = loc() of item 'c'
rec_loc() of person 'i' = loc() of item 'b'
"""
K=[]
L=[]
M=[]
N=[]
O=[]
for i, j in rec_loc.items():
	for p in j[0]:
		for q in j[1]:
			for r in j[2]:
				if i == 'K':
					K.append([i,p,q,r])
				elif i == 'L':
					L.append([i,p,q,r])
				elif i == 'M':
					M.append([i,p,q,r])
				elif i == 'N':
					N.append([i,p,q,r])
				else:
					O.append([i,p,q,r])
rl = []
itm = []
per = []
loc = []
print "Item"+"\t\tPerson"+"\tLocation"
for p in O:
	for q in L:
		for r in M:
			for s in K:
				for t in N:
					rl = [p[0],q[0],r[0],s[0],t[0]]
					itm = [p[1],q[1],r[1],s[1],t[1]]
					per = [p[2],q[2],r[2],s[2],t[2]]
					loc = [p[3],q[3],r[3],s[3],t[3]]
					if (set(['K','L','M','N','O']) == set(rl) and 
						set(['a','b','c','d','e']) == set(itm) and 
						set(['f','g','h','i','j']) == set(per) and 
						set(['k','l','m','n','o']) == set(loc)):
						if((rl[itm.index('d')].lower() == loc[per.index('f')]) and
							rl[loc.index('o')].lower() == loc[per.index('h')] and
							rl[per.index('h')].lower() == loc[per.index('j')] and
							rl[loc.index('m')].lower() == loc[itm.index('e')] and
							rl[itm.index('b')].lower() == loc[itm.index('c')] and
							rl[per.index('i')].lower() == loc[itm.index('b')]):							
							for i in range(5):
								print itm_map[itm[i]]+"\t"+per_map[per[i]]+"\t"+loc_map[loc[i]]						