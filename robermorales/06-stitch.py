#!/usr/bin/python
import sys
import math

doubles = "r,!*^_;"
triples = "Tw"

def dinside(m):
	d = 0
	for i in m:
		if i in doubles:
			d += 1
		if i in triples:
			d += 2
	return d

def p( m, W, H, ct ):
	l = len( m )
	text = l - m.count(" ")
	maxsizex = ( max( W , H ) * ct ) / l
	maxsizey = ( min( W , H ) * ct )
	sizect = min( maxsizex, maxsizey )
	return reduce( lambda x,y:int(x+y),
			map( lambda t: t * math.ceil( (sizect * sizect) / (1. * ct) ),
			map( lambda s: len(s) + dinside(s), m.split(" ")
		)))

N = int(sys.stdin.readline())
i = 1

while i <= N:
	( W, H, ct ) = map( long, sys.stdin.readline().strip().split(" ") )
	m = sys.stdin.readline()[:-1]
	print "Case #{}: {}".format( i, p( m, W, H, ct ) )
	i += 1
