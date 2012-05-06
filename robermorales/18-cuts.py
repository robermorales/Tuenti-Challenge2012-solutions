#!/usr/bin/env python

import sys
from operator import add

# bee is isomorphic with ook
# a. sed -e s/Bee/Ook/g program.bee > program.ook
# b. go to http://ook.heroku.com/ook and paste program.ook
# c. "Input is the number of straight cuts made through a round chocolate cake
#     and output is the maximum number of cake pieces that can be produced."
# d. each cut add n new pieces
# 1 + ( 0 + 1 + 2 + 3 + 4 + ... )
# to sum up, sum the first, the last, and multiply for the size/2

C = int( sys.stdin.readline() )

for c in range( C ):
	n = int( sys.stdin.readline() )
	print "Case #{}: {}".format( c + 1, ( ( n + 1 ) * n ) / 2 + 1 )
