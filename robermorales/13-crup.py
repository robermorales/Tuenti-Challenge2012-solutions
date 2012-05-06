#!/usr/bin/env python

import sys
from operator import mul

cache    = {}
uscache  = {}
mcdcache = {}
factorc  = {}

def move( N, L, p ):
	if not ( N, L, p ) in cache:
		movs = {}
		l = min( L, N - L )
		nnp = 0
		for np in range( l ):
			movs[ ( N, L, L - np - 1 ) ] = nnp
			nnp += 1
			movs[ ( N, L, N - np - 1 ) ] = nnp
			nnp += 1
		if l == L:
			r = range( L, N - l )
		else:
			r = range( 0, L - l )
		for np in reversed( r ):
			movs[ ( N, L, np ) ] = nnp
			nnp += 1
		for k,v in movs.iteritems():
			cache[ k ] = v
	return cache[ N, L, p ]

def untilsame( N, L, p ):
	if not ( N, L, p ) in uscache:
		times = 1
		np = move( N, L, p )
		while np != p:
			np = move( N, L, np )
			times += 1
		uscache[ N, L ,p ] = times
	return uscache[ N, L, p ]

def mcd( a, b ):
	if b > a:
		return mcd( b, a )
	elif not ( a, b ) in mcdcache:
		if b == 1:
			m = b
		if a % b == 0:
			m = b
		else:
			m = mcd( b, int( a / b ) )
		
		mcdcache[ a, b ] = m
	return mcdcache[ a, b ]

def mcm( a, b ):
	return a * b / mcd( a, b )

def t( N, L ):
	if L < ( N / 3 ):
		return t( L * 3, L )
	deck = range( N )[:]
	mod = deck[:]
	equal = False
	times = 0
	while not equal:
		times += 1
		tmp = mod[:]
		for i in range( N ):
			tmp[ move( N, L, i ) ] = mod[ i ]
		mod = tmp
		if mod == deck:
			equal = True
	return times

def factor(n):
	if not n in factorc:
		factors = {}
		i = 2 
		while i <= n and n != 1:
			while n % i == 0:
				try:
					factors[i] += 1
				except KeyError:
					factors[i] = 1
				n = n / i
			i += 1
		factorc[ n ] = factors
	return factorc[ n ]

def lcm( l ):
	base = {}
	for i in l:
		for f, n in factor(i).items():
			try:
				base[f] = max(base[f], n)
			except KeyError:
				base[f] = n
	return reduce(mul, [f**n for f, n in base.items()], 1)

def count( N, L ):
	l = []
	for p in range( N ):
		v = untilsame( N, L, p )
		if v != 1:
			l.append( v )
	if len( l ) == 0:
		return 1

	return lcm( l )

C = int( sys.stdin.readline() )
d = 0
for line in sys.stdin:
	d = d + 1
	cache = {}
	( N, L ) = map( long, line.strip().split( " " ) )
	print "Case #{}: {}".format( d, count( N, L ) )
