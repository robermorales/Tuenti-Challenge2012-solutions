#!/usr/bin/env python

import sys
import itertools
from operator import add,sub,eq

s = []
m = []
u = []

def distance( v1, v2 ):
	return reduce( add, map( abs, itertools.imap( eq, v1, v2 ) ) )

def total_distance( v, a ):
	return reduce( add, itertools.imap( distance, a, itertools.repeat( v ) ) )

R = int( sys.stdin.readline() )
U = int( sys.stdin.readline() )
V = int( sys.stdin.readline() )

for i in range( R ):
	v = sys.stdin.readline().split()
	if   v[0] == 'S':
		s.append( map( int, v[1:] ) )
	elif v[0] == 'M':
		m.append( map( int, v[1:] ) )

for i in range( U ):
	u.append( map( int, sys.stdin.readline().split() ) )

count_calls = 0
for v in u:
	d = [ total_distance( v, a ) for a in [ s, m ] ]
	if d[ 0 ] * len( m ) < d[ 1 ] * len( s ):
		count_calls += reduce( add, v )

print count_calls
