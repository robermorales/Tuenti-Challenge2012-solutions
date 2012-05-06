#!/usr/bin/env python

import sys
from PIL import Image
import math
import itertools

def show_secret():
	im = Image.open( "newspaper.png" )
	pix = im.load()
	w,h = im.size
	print im.mode
	print im.format

	for j in range( h ):
		for i in range( w ):
			r,g,b,a = pix[ i, j ]
			if a == 0:
				for ii in range( i - 5, i + 5 ):
					for jj in range( j + 1 , j + 4 ):
						pix[ ii, jj ] = (0,0,255,255)#r,g,b)

	im.show()

secret =  "the secret has been revealed to solve the challenge which is the twentieth emirp"

is_prime_c = { 0: False, 1: False, 2: True }
is_emirp_c = {}

def is_prime( a ):
	if not a in is_prime_c:
		prime = True
		sqr   = int( math.sqrt( a ) )
		i     = 2
		while prime and i <= sqr:
			prime = a % i != 0
			i += 1
		is_prime_c[ a ] = prime
	return is_prime_c[ a ]

def reverse( i ):
	a = i
	b = 0
	while a > 0:
		m  = a % 10
		b  = b * 10 + m
		a /= 10
	return b

def is_emirp( a ):
	r = reverse( a )
	m = min( a, r )
	if not m in is_emirp_c:
		emirp = a != r and is_prime( a ) and is_prime( r )
		is_emirp_c[ m ] = emirp
	return is_emirp_c[ m ]

def emirp_number( n ):
	step = n
	i = 10
	while step >= 0:
		i += 1
		if is_emirp( i ):
			step -= 1

# to calculate uncomment next line
#print emirp_number( 20 )

# to print it, only print it
print 389
