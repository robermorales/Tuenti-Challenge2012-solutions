#!/usr/bin/python
import sys

for line in sys.stdin:
	v = []
	for op in line.strip().split(" "):
		p = len( v ) - 1
		r = p - 1
		if   op == '.':      print                          v[ p ]  #print
		elif op == '@':            v = v[ :r ] + [ v[ r ] + v[ p ] ]#add
		elif op == '$':            v = v[ :r ] + [ v[ r ] - v[ p ] ]#minus
		elif op == '#':            v = v[ :r ] + [ v[ r ] * v[ p ] ]#multiply
		elif op == '&':            v = v[ :r ] + [ v[ r ] / v[ p ] ]#divide
		elif op == 'conquer':      v = v[ :r ] + [ v[ r ] % v[ p ] ]#modulus
		elif op == 'dance':        v = v[ :r ] + [ v[ p ] , v[ r ] ]#swap
		elif op == 'breadandfish': v = v[ :  ] + [          v[ p ] ]#duplicate
		elif op == 'mirror':       v = v[ :r ] + [ v[ r ],- v[ p ] ]#not
		elif op == 'fire':         v = v[ :r ] + [ v[ r ]          ]#pop
		else:                      v = v[ :  ] + [       int( op ) ]#push
