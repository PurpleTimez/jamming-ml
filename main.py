#!/usr/bin/env/python3

import os

if __name__ == '__main__':

    # check connection env variables are available 

    if os.environ.get('LND_0_RPCSERVER') == None 
        or os.environ.get('LND_0_CERT') == None
        or os.environ.get('LND_0_MACAROON') == None
        or os.environ.get('LND_1_RPCSERVER') == None
        or os.environ.get('LND_1_CERT') == None
        or os.environ.get('LND_1_MACAROON') == None
        or os.environ.get('LND_2_RPCSERVER') == None
        or os.environ.get('LND_2_CERT') == None
        or os.environ.get('LND_2_MACAROON') == None:
            print("No LND env available")


    # start 3 thread to manage LND instances
