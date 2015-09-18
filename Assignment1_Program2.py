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
			for i in graph[next[1]]:
				k=0
				if i[0] not in set(visited):
					q.put((j+k,i[0]))
					visited.append(i[0])
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
def bfs(graph,start,goal):
	q = Queue.PriorityQueue()
	q.put((-1,start))
	visited = []
	path = []
	j = 0
	while True:
		next = q.get()	
		print next
		if next[1] == goal:
			return path
		else:			
			for i in graph[next[1]]:
				if i[0] not in set(visited):
					q.put((j,i[0]))
					visited.append(i[0])
		j+=1
			#print visited
		if q.empty():
			break
	if goal not in path:
		print 'Not found'
		return None		

print 'DFS'
path_dfs = dfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')
print 'BFS'
path_bfs = bfs(seg_dict,'Eastman,_Georgia','Dublin,_Georgia')

#dfs(seg_dict,'Eastman,_Georgia','Eastman,_Georgia')
#print path


f1.close()
f2.close()
f3.close()
f4.close()