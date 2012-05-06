#!/usr/bin/python
import sys

from datetime import datetime

# data

#   1
#
# 6   2
#
#   7
#
# 5   3
#
#   4

l = {
		 0   : [1,1,1,1,1,1,0],
		 1   : [0,1,1,0,0,0,0],
		 2   : [1,1,0,1,1,0,1],
		 3   : [1,1,1,1,0,0,1],
		 4   : [0,1,1,0,0,1,1],
		 5   : [1,0,1,1,0,1,1],
		 6   : [1,0,1,1,1,1,1],
		 7   : [1,1,1,0,0,0,0],
		 8   : [1,1,1,1,1,1,1],
		 9   : [1,1,1,1,0,1,1],
		-1   : [0,0,0,0,0,0,0],
	}

# calculated data

ledon = {}
for k,v in l.iteritems():
	ledon[k] = v.count(1)

def route(i,j):
	s = 0
	for a in range( i, j+1 ):
		s += ledon[ a ]
	return s

a59 = route(0,5) * 10 + route(0,9) * 6
a23 = route(0,1) * 10 + route(2,2) * 4 + route(0,9) * 2 + route(0,3)

clock2 = {}
clock1 = {}

for k,v in l.iteritems():
	for k2,v2 in l.iteritems():
		clock2[    k, k2 ] = map( lambda x,y: x == 0 and y == 1, v, v2 ).count( True )
		clock1[ k, k2 ] = v2.count( 1 )

# dos digitos, un parpadeo
# on, 59, 00 -> 2+1
def aps( a, prev, c ):
	if( prev == -1 ):
		return a[ -1, c / 10 ] + a[ -1, c % 10 ]
	return a[ prev / 10, c / 10 ] + a[ prev % 10, c % 10 ]

# un digito, los parpadeos necesarios
# on, 0, 2 ==> 4
def acc( a, i, j ):
	s = 0
	for b in range( i, j ):
		s = s + a[ b, b + 1 ]
	return s

# dos digitos, los parpadeos necesarios
# on, 00, 59 -> 97?
def acc2( a, i, j ):
	s = 0
	for c in range( i, j ):
		s = s + aps( a, c, c + 1 )
	return s

# dos digitos, los parpadeos necesarios y la vuelta
def acc2v( a, i, j ):
	return acc2( a, i, j ) + aps( a, j, i )

def info( a ):
	return{
		'59' : affp( a, 0, 59 ),
		'23' : affp( a, 0, 23 )
	}

def desc( s ):
	#( m,  h,  d,  rs,  rm,  rh  )
	return ( s/60, s/(60*60), s/(60*60*24), s % 60, (s/60)%60, (s/(60*60))%24)

def count(a,s):
	( m,  h,  d,  rs,  rm,  rh  ) = desc( s )
	( m1, h1, d1, rs1, rm1, rh1 ) = desc( s - 1 )

	# abs * dos digitos con vuelta
	seconds = m * a59        #minutos completos
	minutes = h * a59 * 60   #horas completas
	hours   = d * a23 * 3600 #dias completos

	# ticks * dos digitos sin vuelta
	for i in range(0, rs + 1):
		seconds += ledon[i/10] + ledon[i%10]
	for i in range(0, rm):
		minutes += (ledon[i/10] + ledon[i%10])*60
	for i in range(0, rh):
		hours += (ledon[i/10] + ledon[i%10])*60*60

	# remain anterior * dos digitos directo
	minutes += (ledon[rm/10] + ledon[rm % 10])*(rs+1)
	hours += (ledon[rh/10] + ledon[rh % 10])*(s % 3600 + 1)
	return hours + minutes + seconds

def delta( a, s ):
	( m,  h,  d,  rs,  rm,  rh  ) = desc( s )
	
	seconds = m * acc2v(a,0,59)#minutos completos
	minutes = h * acc2v(a,0,59)#horas completas
	hours   = d * acc2v(a,0,23)#dias completos

	seconds += (acc2( a, 0, rs))#segundos restantes
	minutes += (acc2( a, 0, rm))#minutos restantes
	hours   += (acc2( a, 0, rh))#horas restantes

	#encendido
	seconds += 12
	minutes += 12
	hours   += 12
	
	return hours + minutes + seconds #+ 6 * a[ 10, 0 ]

for line in sys.stdin:
	if line != '' and not line.isspace():
		( init, end ) = map(
			lambda a: datetime.strptime( a.strip(), "%Y-%m-%d %H:%M:%S"),
			line.split( " - " )
		)
		s = (end - init).seconds + (end - init).days * 24 * 60 * 60
		print count( clock1, s ) - delta( clock2, s )
