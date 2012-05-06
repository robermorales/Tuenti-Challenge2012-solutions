#!/usr/bin/env python

import sys

comment = "a541714a17804ac281e6ddda5b707952"
qr      = "ed8ce15da9b7b5e2ee70634cc235e363"
lsb     = "62cd275989e78ee56a81f0265a87562e"

#http   = "vdc8tvct04lfkh0pjd381e5tp1"
#"contest=vdc8tvct04lfkh0pjd381e5tp1"

k = [ qr, lsb, comment ]

k.append( sys.stdin.readline().strip() )

a = reduce( lambda k1,k2:[ "%x" % ((int(k1[i],16) + int(k2[i],16)) % 16) for i,c in enumerate(k1) ] , k )
print ''.join(a)
