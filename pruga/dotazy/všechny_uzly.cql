//START n=node(*) RETURN n

START n=node(*)
MATCH n-[r?]-()
RETURN n,r
