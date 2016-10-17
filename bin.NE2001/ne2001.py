#!/usr/local/python-2.7.2/bin/python

import os
import sys
from commands import getoutput
from pprint import pprint

path = os.environ["NE2001"]
input_dir = os.path.join(path,"input.NE2001")
executable = os.path.join(path,"bin.NE2001","NE2001")

def in_ne2001_directory(func):
    def wrapped(*args,**kwargs):
        cws = os.getcwd()
        os.chdir(input_dir)
        try:
            retval = func(*args,**kwargs)
        except Exception as error:
            os.chdir(cws)
            raise error
        os.chdir(cws)
        return retval
    return wrapped

def parse_output(output):
    if "Aborted" in output:
        raise Exception(output)
    lines = output.splitlines()
    lines = [i for i in lines if i.lstrip()[0]!="#"]
    out = {}
    for line in lines:
        s = line.split()
        out[s[1]] = float(s[0])
    return out
    
@in_ne2001_directory
def ne2001(gl,gb,DMD,mode):
    """ NE2001 exectuable
        gl - Galactic longitude (deg)
        gb - Galactic latitude (deg)
        DM/D - DM or Distance(pc cm^{-3} or kpc)
        ndir = 1 (DM->D) or -1 (D->DM)
    returns dictionary with output values
    """
    assert mode in [1,-1], "mode must be 1 or -1"
    output = getoutput("%s %f %f %f %d"%(executable,gl,gb,DMD,mode))
    print output
    return parse_output(output)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "Usage: %s gl gb DMD mode"%(sys.argv[0].split("/")[-1])
        usage = getoutput(executable).splitlines()
        print "\n".join(usage[1:])        
    else:
        gl = float(sys.argv[1])
        gb = float(sys.argv[2])
        DMD = float(sys.argv[3])
        mode = int(sys.argv[4])
        ne2001(gl,gb,DMD,mode)
    
    


