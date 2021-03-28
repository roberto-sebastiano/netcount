# netcount

Problem:
To count tcp established connections on a TCP port, a common recipe is:
netstat -tapn | grep ESTABLISHED | grep :80
But this command gives you the connections that you have in that precise moment.
What if you have lots of short living connection ? You miss them from that count 

Solution: ./netcount -p 80

:)

Netcount: A tool to counts the number of connections per second on a specific tcp port

Requires python3, iptables, netstat, conntrack and root privileges

Tested on Centos7/8 and Ubuntu 14.04/18.04/20.04
