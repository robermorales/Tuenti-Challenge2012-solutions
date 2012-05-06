#!/usr/bin/env python

import sys
import math

# radio desde 0,0 a x,y
def r( x, y ):
	return math.sqrt( x**2 + y**2 )

# angulo theta de eje X a x,y
def t( x, y ):
	return math.atan2( y, x )

#r,theta de x,y
def rt( x, y ):
	return ( r( x, y ), t( x, y ) )

#x,y de r,theta
def xy( rad, the ):
	return rad * math.cos( the ), rad * math.sin( the )

def extractrtpi( ran, mint, maxt, prev, post ):
	outran = {}
	for k,c in ran.iteritems():
		m,M = k
		if maxt >= m and mint <= M:
			if maxt <= M and mint >= m:
				outran[ m, mint ] = c + prev
				outran[ maxt, M ] = c + post
			elif mint < m:
				outran[ maxt, M ] = c + post
			elif maxt > M:
				outran[ m, mint ] = c + prev
		elif maxt < m:
			outran[ m, M ] = c + post
		elif mint > M:
			outran[ m, M ] = c + prev

	outran2 = {}
	for k,c in outran.iteritems():
		m,M = k
		if( m <= M ):
			outran2[ m, M ] = c

	return outran2


def extractrt( ran, mint, maxt ):
	if mint < - math.pi / 2:
		outran1 = extractrtpi(    ran , mint + math.pi        ,        math.pi / 2 + 1 ,  0,  0 )
		outran2 = extractrtpi( outran1,      - math.pi / 2 - 1, maxt                   , -1, +1 )
	elif maxt > math.pi / 2:
		outran1 = extractrtpi(    ran ,      - math.pi / 2 - 1, maxt - math.pi         ,  0,  0 )
		outran2 = extractrtpi( outran1, mint                  ,        math.pi / 2 + 1 , -1, +1 )
	else:
		outran2 = extractrtpi(    ran , mint                  , maxt                   , -1, +1 )
	
	return outran2

def calculatevertex( x, y, vx, vy, edges ):
	rad,the = rt( vx - x, vy - y )
	step = math.pi / edges
	vertex = []
	for i in range( edges ):
		cx,cy = xy( rad, the + i * step )
		nr,nt = rt( x + cx, y + cy )
		vertex.append( nt )
	return vertex

def extractch( ran, edges, p ):
	if ran == {}:
		return ran
	
	outran = ran.copy()
	x, y, vx, vy = p
	rad,the = rt( vx - x, vy - y )
	vertex = calculatevertex( x, y, vx, vy, edges )

	mint = min( vertex )
	maxt = max( vertex )
	ran = extractrt( outran, mint, maxt )
	
	return ran

def extract( ran, ing ):
	if ran == {}:
		return ran

	outran = ran.copy()
	edges = ing[ 'edges' ]
	pos = ing[ 'pos' ]
	i = 0
	for p in pos:
		outran = extractch( outran, edges, p )
		i += 1
	return outran

def can( cx, cy, r, ings ):
	for l,i in ings.iteritems():
		for n,p in enumerate( i[ 'pos' ] ):
			x, y, vx, vy = p
			i[ 'pos' ][ n ] = [ x - cx, y - cy, vx - cx, vy - cy ]

	ran = { (-math.pi/2,math.pi/2) : 0 }# [0,pi), the only range of current possibilities, 0 offset for earlier
	
	for l,ing in ings.iteritems():
		ran = extract( ran, ing )

	for k,v in ran.iteritems():
		if v == 0:
			return True
	
	return False

# main

C = int( sys.stdin.readline() )

for c in range( C ):
	cx,cy,rad = map( float, sys.stdin.readline().split() )
	N = int( sys.stdin.readline() )
	ings = {}
	for n in range( N ):
		label,edges,count = sys.stdin.readline().split()
		pos = []
		for i in range( int( count ) ):
			pos.append( map( float, sys.stdin.readline().split() ) )
		ings[ label ] = { 'edges' : int( edges ), 'pos': pos }
	print "Case #{}: {}".format( c + 1, str( can( cx, cy, rad, ings ) ).upper() )
