import sys
import Queue

start_city = sys.argv[1] 
end_city = sys.argv[2] 
routing_option = sys.argv[3]
routing_algo = sys.argv[4]

f1 = open('city-gps.txt','r')
f2 = open('road-segments.txt','r')

cities = []
for city in f1:
	cities.append(city.split())
seg = []
for segments in f2:
	seg.append(segments.split())

city_dict = {}
seg_dict = {}

#Creating dictionary to store cities and their data which can be reached from a city. 
for segments in seg:
	if len(segments) != 5:
		segments = [segments[0],segments[1],int(segments[2]),9999,segments[3]]
	else:
		segments = [segments[0],segments[1],int(segments[2]),int(segments[3]),segments[4]]
	if segments[0] not in seg_dict:
		seg_dict[segments[0]] = [(segments[1],segments[2],segments[3],segments[4])]
	else:
		seg_dict[segments[0]].append((segments[1],segments[2],segments[3],segments[4]))
	if segments[1] not in seg_dict:
		seg_dict[segments[1]] = [(segments[0],segments[2],segments[3],segments[4])]
	else:
		seg_dict[segments[1]].append((segments[0],segments[2],segments[3],segments[4]))

#Creating dictonary to store latitude and longitude of a city
for city in cities:
	city_dict.update({str(city[0]) : (float(city[1]),float(city[2]))})

#Logic to find path of a child to connect to its parent
def find_parent(parent_dict,child,parent_target,path):
	if parent_dict[child] == parent_target:
		path.append(parent_target)
		return path
	else:
		path.append(parent_dict[child])
		return find_parent(parent_dict,parent_dict[child],parent_target,path)
#DFS Logic
def dfs(graph,start,goal):
	q = Queue.PriorityQueue()
	q.put((-1,start))
	visited = []
	parent_dict = {}
	path = []
	j = -1
	while True:
		next = q.get()
		if next[1] == goal:
	#		print parent_dict
			path = find_parent(parent_dict,goal,start,[goal])
			return path
		else:
			tmp = []
			for i in graph[next[1]]:
				if i[0] not in set(visited):
					tmp.append(i)
			tmp.sort(key = lambda x:x[1])
			for i in tmp:
				k=0
				q.put((j+k,i[0]))
				parent_dict[i[0]] = next[1]
				visited.append(i[0])
				k-=1
		j -= 1
		if q.empty():
			break
	if goal not in path:
		print 'Not found'
		return None
#BFS Logic
def bfs(graph,start,goal):
	q = Queue.PriorityQueue()
	q.put((-1,start))
	visited = []
	path = []
	parent_dict = {}
	j = 0
	while not q.empty():
		next = q.get()
		#print next
		if next[1] == goal:
	#		print parent_dict
			path = find_parent(parent_dict,goal,start,[goal])
			return path
		else:
			k=j
			tmp = []
			for i in graph[next[1]]:
		#		print i
				if i[0] not in set(visited):
					tmp.append(i)
			tmp.sort(key = lambda x:x[1])
			#Give first priority to nearest city to go for
			for i in tmp:
				q.put((k,i[0]))
				parent_dict[i[0]] = next[1]
				visited.append(i[0])
		j+=1
	#print visited

	if goal not in path:
		print 'Not found'
		return None

total_time = 0
total_dist = 0
if routing_algo == 'bfs':
#	print 'BFS'
	path_bfs = bfs(seg_dict,start_city,end_city)
	path_bfs.reverse()
	print ' '.join(path_bfs)
	
	c = 0
	try:
		for i in path_bfs:
			print i
			for j in seg_dict[i]:
				if j[0] == path_bfs[c+1]:
					print str(c+1)+' Take '+str(j[3])+" from "+i+" to "+j[0]+" for distance "+str(j[1])+" at max speed "+str(j[2])
					total_dist += int(j[1])
					total_time += float(j[1])/j[2]
					break
			c+=1
	except Exception:
		pass
		
	print "Total"
	print str(total_dist)+" "+str(total_time)+" ".join(path_bfs)
	'''
	for i in path_bfs:
		for j in seg_dict[i]:
			print j
	'''
elif routing_algo == 'dfs':
#	print 'DFS'
	path_dfs = dfs(seg_dict,start_city,end_city)
	path_dfs.reverse()
	print ' '.join(path_dfs)
	c = 0
	try:
		for i in path_dfs:
			for j in seg_dict[i]:
				if j[0] == path_dfs[c+1]:
					print str(c+1)+' Take '+str(j[3])+" from "+i+" to "+j[0]+" for distance "+str(j[1])+" at max speed "+str(j[2])
					total_dist += int(j[1])
					total_time += float(j[1])/j[2]
			c+=1
	except Exception:
		pass
		
	print "Total"
	print str(total_dist)+" "+str(total_time)+" ".join(path_dfs)
else:
	print 'No path found'

#path_dfs = dfs(seg_dict,'Bloomington,_Indiana','Indianapolis,_Indiana')
#path_dfs.reverse()
#print path_dfs
#path_dfs = dfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')
#print 'BFS'
#path_bfs = bfs(seg_dict,'Bloomington,_Indiana','Indianapolis,_Indiana')
#path_bfs = bfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')

#dfs(seg_dict,'Eastman,_Georgia','Eastman,_Georgia')
#path_bfs.reverse()
#print path_bfs


f1.close()
f2.close()