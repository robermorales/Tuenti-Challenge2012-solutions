#!/usr/bin/env python

import sys
import string
import binascii

def parity( code, i ):
	u = 0
	s = i
	while s < len( code ):
		u += code[ max( s, i + 1 ) : s + i + 1 ].count( '1' )
		s += 2 * ( i + 1 )
	return u

def check( code ):
	errors = ""
	j = 1
	while j <= len( code ):
		u = parity( code, j - 1 )
		if str( u % 2 ) == code[ j - 1 ]:
			errors = "0" + errors
		else:
			errors = "1" + errors
		j *= 2

	if errors == "":
		return 0
	return int( errors, 2 )

def code2data( codestr ):
	code = [ c for c in codestr ]

	e = check( code ) - 1
	if e >= 0 and e < len( code ):
		if  code[ e ] == '0':
			code[ e ]  = '1'
		else:
			code[ e ]  = '0'

	data = []
	for i,c in enumerate( code ):
		if( bin( i + 1 ).count( "1" ) != 1 ):
			data.append( c )
	return ''.join( data )

for line in sys.stdin:
	line = line.strip()
	byte = 7
	char = 2 * byte


	if len( line ) % char == 0:
		s = ''
		a = 0
		while a < len( line ):
			for i in [ a, a + byte ]:
				s += "%x" % int( code2data( line[ i : i + byte ] ), 2 )
			a += char

		s = binascii.unhexlify( s )

		if all( map( lambda c : c in string.printable, s ) ):
			print s

		else:
			print "Error!"
	else:
		print "Error!"
