#!/usr/bin/env python
# let's cheat at scrabble

import sys

# data

score={ "A":  1,
		"B":  3,
		"C":  3,
		"D":  2,
		"E":  1,
		"F":  4,
		"G":  2,
		"H":  4,
		"I":  1,
		"J":  8,
		"K":  5,
		"L":  1,
		"M":  3,
		"N":  1,
		"O":  1,
		"P":  3,
		"Q": 10,
		"R":  1,
		"S":  1,
		"T":  1,
		"U":  1,
		"V":  4,
		"W":  4,
		"X":  8,
		"Y":  4,
		"Z": 10  }

# functions

def sp(w, r, h):
	#if( not w[ 0 ] in rack or not word[ 0 ] in hor ):
		#return False
	# not set(w).isdisjoint(set(h))
	# not set(w).isdisjoint(set(r))
	if( len( w ) <= 1 ):
		return False
	rc = { l : ( w.count( l ) - r.count( l ) ) for l in set( w ) }
	f = 0
	l = '?'
	for i,v in rc.iteritems():
		if v > 1:
			return False
		if v == 1:
			if f > 0 or not i in h:
				return False
			l = i
			f = f + 1
	return ( f == 1 ) and ( l in h )

def sc(word):
	return sum([score[c] for c in word])

def wr( filename ):
	a = {}
	for l in open( filename, 'r' ):
		w = l.strip().upper()
		s = ''.join( sorted( w ) )
		if not s in a:
			a[ s ] = []
		a[ s ].append( w )
	return a

# main

ws = wr( 'descrambler_wordlist.txt' )
N = int( sys.stdin.readline() )

for line in sys.stdin:
	( r, h ) = line.strip().split(" ")
	p = ( ( sc( w ), w, l ) for w, l in ws.iteritems() if sp( w, r, h ) )
	fp = sorted( p )
	( sm, wm, lm ) = max( fp )
	m = []
	for ( s, w, l ) in fp:
		if s == sm:
			m = m + l
	print sorted( m )[ 0 ], sm
