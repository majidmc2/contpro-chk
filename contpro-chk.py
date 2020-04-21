import os
import argparse


def logo():
    my_log = """
-------------------------------------------------------------------------
 ██████  ██████  ███    ██ ████████ ██████  ██████   ██████             ██████ ██   ██ ██   ██ 
██      ██    ██ ████   ██    ██    ██   ██ ██   ██ ██    ██           ██      ██   ██ ██  ██  
██      ██    ██ ██ ██  ██    ██    ██████  ██████  ██    ██           ██      ███████ █████   
██      ██    ██ ██  ██ ██    ██    ██      ██   ██ ██    ██           ██      ██   ██ ██  ██  
 ██████  ██████  ██   ████    ██    ██      ██   ██  ██████   ███████   ██████ ██   ██ ██   ██ 
                                                                                                                                                                     
                    Owner: Majid Iranpour
                     twitter: @_majidmc2
-------------------------------------------------------------------------
"""
    print(my_log)


def connection(uri, grep=None):
    if grep:
        cmd = 'adb shell content query --uri {uri} | grep -i "{grep}"'.format(uri=uri, grep=grep)
    else:
        cmd = 'adb shell content query --uri {uri}'.format(uri=uri)
    print('uri ==> ', uri, '\n', os.system(cmd), '\n', '====================')


def main():
    parser = argparse.ArgumentParser(prog="contpro_chk",
                                     usage="python3 contpro_chk.py [options]",
                                     description="""This script checks all of your Android Content-Providers and 
                                     shows output of them""")
    parser.add_argument('-u', nargs='?', type=str, help='A spacial URI')
    parser.add_argument('-l', nargs='?', type=str, help='List of URIs in a txt format file')
    parser.add_argument('-g', nargs='?', type=str, help='Grep on a spacial name and if it find then show output')
    args = parser.parse_args()

    if args.u:
        logo()
        if args.g:
            connection(args.u, args.g)
        else:
            connection(args.u)
    elif args.l:
        try:
            with open(args.l, 'r') as f:
                logo()
                for uri in f.readlines():
                    if args.g:
                        connection(uri, args.g)
                    else:
                        connection(uri)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
