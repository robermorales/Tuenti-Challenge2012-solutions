#!/usr/bin/python
import sys

# data conf

initialkey = '0'
same = 500
hor = 200
ver = 300
dia = 350
delay = 100

pad = {
		'1':(" ","1"),
		'2':("A","B","C","2"),
		'3':("D","E","F","3"),
		'4':("G","H","I","4"),
		'5':("J","K","L","5"),
		'6':("M","N","O","6"),
		'7':("P","Q","R","S","7"),
		'8':("T","U","V","8"),
		'9':("W","X","Y","Z","9"),
		'0':("0"),
		'^':("^")
}

grid = {
		'1':(0,0),
		'2':(1,0),
		'3':(2,0),
		'4':(0,1),
		'5':(1,1),
		'6':(2,1),
		'7':(0,2),
		'8':(1,2),
		'9':(2,2),
		'0':(1,3),
		'^':(2,3)
}

# functions

def dist((x,y),(x2,y2)):
	if( x == x2 and y != y2 ):
		return abs(y - y2) * ver
	elif( x != x2 and y == y2):
		return abs(x - x2) * hor
	elif( x != x2 and y != y2 ):
		dx = abs(x-x2)
		dy = abs(y-y2)
		d = min( dx, dy )
		r = max( dx, dy ) - d
		if( dx > dy ):
			return r * hor + d * dia
		else:
			return r * ver + d * dia
	elif( (x,y) == (x2,y2) ):
		return same

# data generated

keys = {}
for k, v in pad.iteritems():
	i = 1
	for l in v:
		keys[ l ] = { 'key' : k, 'steps': i, 'time': i*delay }
		i = i + 1

trans = {}
for k, v in grid.iteritems():
	for k2, v2 in grid.iteritems():
		trans[ (k,k2) ] = dist(v,v2)

# main

def write( c, prev, change_case ):
	if( c == '\n' ):
		return ( 0, prev )
	k = keys[ c.upper() ]
	if( change_case ):
		( t1, pkey1 ) = write( '^', prev, False )
		( t2, pkey2 ) = write( c.lower(), pkey1, False )
		return ( t1 + t2, pkey2 )
	else:
		return ( trans[ ( prev, k['key'] ) ] + k['time'], k['key'],  )

N = int(sys.stdin.readline())

for line in sys.stdin:
	( time, pkey, prevupcase ) = ( 0, initialkey, False )
	for c in line:
		if( c.lower() >= 'a' and c.upper() <= 'Z' ):
			upcase = c != c.lower()
			( t, pkey ) = write( c, pkey, prevupcase != upcase )
			prevupcase = upcase
		else:
			( t, pkey ) = write( c, pkey, False )
		time = time + t
	print time
