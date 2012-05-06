#!/usr/bin/python
import sys

# data

trades = []

# functions

def evil( trades ):
	( mint, maxt, maxdiff ) = ( 0, 0, 0 )
	for i,a in enumerate( trades ):
		for j,b in enumerate( trades ):
			if( j > i ):
				diff = b - a
				if ( diff > maxdiff ):
					( mint, maxt, maxdiff ) = ( i, j, diff )
	return ( mint*100, maxt*100, maxdiff )

# main

for line in sys.stdin:
	trades.append( int( line ) )

( mint, maxt, maxdiff ) = evil( trades )

print "{} {} {}".format( mint, maxt, maxdiff )
