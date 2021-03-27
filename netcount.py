#!/usr/bin/python3
import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="tcp port to count connections on", type=int, required=True)
args = parser.parse_args()

port = args.port

if not ((port > 0) and (port < 65535)):
    print("Invalid port {port}".format(port=port))
    sys.exit(1)

def main():
    # netstat -tapn | grep ESTA | tr -s " " | cut -d " " -f 4 | grep :80 | wc -l
    netstat_count = subprocess.check_output("""netstat -tapn | grep ESTA | tr -s " " | cut -d " " -f 4 | grep :80 | wc -l""", shell=True, text=True)
    #netstat_count = subprocess.check_output("ls /", shell=True, text=True)
    print("Netstat count on port {port} (instantaneous) : {ncount}".format(port=80, ncount=netstat_count))



if __name__ == "__main__":
    main()