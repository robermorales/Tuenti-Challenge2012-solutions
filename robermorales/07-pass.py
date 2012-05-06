#!/usr/bin/python
import sys

g      = []
labels = []
lines  = []
paths  = []

def addnode( node ):
	if not ( node ).isspace() and not node in labels:
		g.append( set([]) )
		labels.append( node )

def addnodes( line ):
	map( addnode, line )

def addline( line ):
	for i in range( 0, len(line) - 1 ):
		la = labels.index( line[ i     ] )
		lb = labels.index( line[ i + 1 ] )
		g[ lb ].add( la )

def calculatepaths( g, path ):
	if len( path ) == len( labels ):
		s = ''
		for p in path:
			s += labels[p]
		print s
	else:
		for k, v in enumerate( g ):
			if not k in path and len( v ) == 0:
				path2 = path[:] + [ k ]
				g2 = g[:]
				for k2, v2 in enumerate( g2 ):
					g2[ k2 ] = v2 - set([ k ])
				calculatepaths( g2, path2 )

map( lambda l: lines.append( l.strip() ), sys.stdin )
map( addnodes, lines )
map( addline, lines )

calculatepaths( g, [] )

