# -*- coding: utf-8 -*-

ltbtools_version = "0.3"

import struct
import sys

def read_strings(ofs, start_line, lines, b):
    for i in xrange(start_line+lines):
        loc = struct.unpack("q", str(b[ofs:ofs+8]))[0]
        end = b.find(chr(0),loc)
        s = str(b[loc:end])
        s = s.replace('\n','\\n')
        if i>=start_line:
            print "%s" % (s)
        ofs+=8

def write_strings(ofs, start_line, lines, b):
    ofs += start_line*8
    loc = struct.unpack("q", str(b[ofs:ofs+8]))[0]

    for s in sys.stdin:
        s = s.rstrip('\r\n')
        s = s.replace('\\n','\n')

        w = bytearray(s)
        w.append(0)

        # pad to 8 bytes
        while len(w)%8!=0:
            w.append(0)

        # paste string
        for i in xrange(len(w)):
            b[loc+i] = w[i]

        # write string offset
        bytes = struct.pack("q", loc)
        for i in xrange(8):
            b[ofs+i] = bytes[i]

        ofs += 8
        loc += len(w)

if __name__=='__main__':

    if len(sys.argv)<2:
        print "WayForward's Adventure Time text resource files (.ltb) tool ver. %s" % ltbtools_version
        print "Usage: ltbtools.py localization.ltb > strings.txt"
        print "       ltbtools.py --write localization.ltb < strings.txt "
    else:
        write = False

        for arg in sys.argv:
            if arg=='--write':
                write = True
            else:
                fname = arg

        ofs = 0x40
        start_line = 2294
        lines = 2294

        b = bytearray(file(fname,'rb').read())
        if write:
            write_strings(ofs, start_line, lines, b)
            file(fname, "wb").write(b)
        else:
            read_strings(ofs, start_line, lines, b)
