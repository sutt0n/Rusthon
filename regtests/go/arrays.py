"""array types"""

def main():
	a = []int(1,2,3)
	TestError( a[0]==1 )
	TestError( len(a)==3 )
	a.append( 4 )
	TestError( len(a)==4 )

	b = [2]int(100,200)
	TestError( b[0]==100 )
	TestError( b[1]==200 )

	c = a[:2]
	TestError( len(c)==2 )

	d = range(10)
	TestError(len(d)==10)
	d.append(99)
	TestError(len(d)==11)

	e = range(2,10)
	TestError(len(e)==8)

	#f = range(2,10, 2)
	#TestError(len(f)==4)
