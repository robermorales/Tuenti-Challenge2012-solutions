#!/usr/bin/python
import sys
import hashlib
import string

h     = hashlib.md5()
tl    = { i:i for i in (string.lowercase + string.uppercase) }
q     = sys.stdin.readline().strip()
lines = [ l for l in sys.stdin ]

for line in reversed( lines ):
	tl2 = tl.copy()
	for a in line.strip().split( "," ):
		( s, t ) = a.split( "=>" )
		tl2[ s ] = ''.join( map( tl.get, t ) )
	tl = tl2

map( h.update, map( tl.get, q ) )

print h.hexdigest()
