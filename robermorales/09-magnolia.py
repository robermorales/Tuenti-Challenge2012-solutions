#!/usr/bin/python
import sys

# data
docs = 800

# functions

def dlp( W, N ):
	n = int( N )
	d = 0
	while n > 0 and d < docs:
		d += 1
		lines = open( "documents/{:0>4}".format( d ), 'r' ).readlines()
		l = 0
		while n > 0 and l < len( lines ):
			line = lines[ l ].strip().upper()
			l += 1
			if W in line:
				words = line.split(" ")
				p = 0
				while n > 0 and p < len( words ):
					if words[ p ] == W:
						n = n - 1
					p += 1
	print "{}-{}-{}".format( d, l, p )

# main

C = int( sys.stdin.readline() )
for i in range( C ):
	( W, N ) = sys.stdin.readline().strip().upper().split(" ")
	dlp( W, N )
