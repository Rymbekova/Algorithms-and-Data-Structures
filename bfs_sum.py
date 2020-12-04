BFS(G : graph; x : vertex, sum : total sum of all nodes)
	Q := NewQueue(); 
	sum = 0 or sum = []
	Enqueue(Q, x);
	mark x as discovered 
	sum +=x or sum.append(x) then sum of the list
	while not Empty(Q) do
		u := Dequeue(Q);
		visit the vertex u 
		for each v in AdjSet(G, u)
			if (v is not marked) then
			Enqueue(Q, v)
			mark v as discovered