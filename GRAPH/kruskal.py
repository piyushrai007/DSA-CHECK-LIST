import disjoint
def kruskal(adj,v):
    a = disjoint(v)

    adj = sorted(adj)
    mst = 0
    for wt,u,v in adj:
        if a.findparent(u)!=a.findparent(v):
            mst+=wt
            a.unionbyrank(u,v)

