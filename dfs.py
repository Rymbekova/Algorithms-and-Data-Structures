DFS(G: graph, u: vertex, sum):
	if u is not visited: DFS(u)
	mark u as visited
	print new line 
	sum += 0
	for each v in AdjSet(G, u):
		mark as visited 
		sum +=1
		print v
		if v is not visited: DFS(v)
	return 

