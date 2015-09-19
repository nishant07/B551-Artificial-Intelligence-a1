import sys
import Queue
'''
start_city = sys.argv[1] 
end_city = sys.argv[2] 
routing_option = sys.argv[3]
routing_algo = sys.argv[4]
'''
f1 = open('city-gps.txt','r')
f2 = open('road-segments.txt','r')
f3 = open('seg_dict.txt','w')
f4 = open('city_dict.txt','w')
cities = []
#t = []
for city in f1:
	#t.append(city.split()[0])
	cities.append(city.split())
	
#print t	
#print len(cities)
seg = []
for segments in f2:
	seg.append(segments.split())
print len(seg)
city_dict = {}
seg_dict = {}
for segments in seg:	
	if len(segments) != 5:
		segments = [segments[0],segments[1],int(segments[2]),9999,segments[3]]
	#	seg_dict.append([segments[0],segments[1],int(segments[2]),9999,segments[3]])
	else:
		segments = [segments[0],segments[1],int(segments[2]),int(segments[3]),segments[4]]
	#	seg_dict.append([segments[0],segments[1],int(segments[2]),int(segments[3]),segments[4]])
	
	if segments[0] not in seg_dict:
		seg_dict[segments[0]] = [(segments[1],segments[2],segments[3],segments[4])]
	else:
		seg_dict[segments[0]].append((segments[1],segments[2],segments[3],segments[4]))

	
	if segments[1] not in seg_dict:
		seg_dict[segments[1]] = [(segments[0],segments[2],segments[3],segments[4])]
	else:
		seg_dict[segments[1]].append((segments[0],segments[2],segments[3],segments[4]))

print len(seg_dict)
for city in cities:
		city_dict.update({str(city[0]) : (float(city[1]),float(city[2]))})
print len(city_dict)		
for i,j in city_dict.items():
	f4.write(i+str(j)+"\n")
#print city_dict
for i,j in seg_dict.items():
	f3.write(i+str(j)+"\n")
total_dist = 0
total_time = 0
def dfs(graph,start,goal):
	q = Queue.PriorityQueue()
	q.put((-1,start))
	visited = []
	path = []
	j = -1
	while True:
		next = q.get()	
		print next
		print next[1]
		if next[1] == goal:
			return path
		else:
			tmp = []
			for xx in graph[next[1]]:				
				if xx[0] not in set(visited):
					tmp.append(xx[0])
			tmp.sort(key = lambda x:x[1])
			print "tmp"
			print tmp	
			for i in tmp:
				k=0
				q.put((j+k,i[0]))
				#parent_dict[i[0]] = next[1]
				visited.append(i[0])					#q.put((j+k,i[0]))
					#visited.append(i[0])
				k-=1
		j -= 1
			#print visited
		if q.empty():
			break
	if goal not in path:
		print 'Not found'
		return None		
'''
def dfs(graph, start, goal, path=None):
	print path
	if path is None:
		path = [start]
	if start == goal:
		return path
	for next in graph[start]:
		print "Next:"+next[0]
		if next not in path:
			dfs(graph, next[0], goal, path.append(next[0]))
'''
def find_parent(parent_dict,child,parent_target,path=None):
	print "in find"
	if path == None:
		path = [child]
	for i in parent_dict.items():
		if i[1] == parent_target:
			print 'yes'
			return path
		if i[1] != parent_target:
			print i[1]
			find_parent(parent_dict,i[1],parent_target,path.append(i[1]))
def bfs(graph,start,goal):
	q = Queue.PriorityQueue()
	q.put((-1,start))
	visited = []
	path = []
	parent_dict = {}
	j = 0
	while not q.empty():
		next = q.get()	
		print next
		if next[1] == goal:
			print parent_dict
			path = find_parent(parent_dict,goal,start)
			return path
		else:
			k=j
			tmp = []
			for i in graph[next[1]]:
				print i
				if i[0] not in set(visited):
					tmp.append(i)				
			tmp.sort(key = lambda x:x[1])			
			for i in tmp:
				q.put((k,i[0]))
				parent_dict[i[0]] = next[1]
				visited.append(i[0])
		j+=1
			#print visited
	
	if goal not in path:
		print 'Not found'
		return None		

'''
if routing_algo == 'bfs':
	path_bfs = bfs(seg_dict,start_city,end_city)
elif routing_algo == 'dfs'
	path_dfs = dfs(seg_dict,start_city,end_city)	
'''
#print 'DFS'
#path_dfs = dfs(seg_dict,'Bloomington,_Indiana','Indianapolis,_Indiana')
path_dfs = dfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')
#print 'BFS'
#path_dfs = bfs(seg_dict,'Bloomington,_Indiana','Indianapolis,_Indiana')
path_bfs = bfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')

#dfs(seg_dict,'Eastman,_Georgia','Eastman,_Georgia')
print path_bfs


f1.close()
f2.close()
f3.close()
f4.close()