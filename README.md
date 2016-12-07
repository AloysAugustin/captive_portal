# captive_portal
A very simple captive portal system using Flask and netfilter

This set of scripts sets up a captive portal for a WiFi network. All web requests from the users are redirected to
the local machine and all the traffic to the outside is rejected as long as the user has not logged in. Once the 
user has logged in, his traffic is accepted.

This captive portal is correctly detected by OS X, iOS and Android which automatically open the login page.

The start.sh script (to run as root) allows to start all the services required, i.e. hostapd, dnsmasq (which must be installed)
in a tmux (useful for debugging)

### Bugs

- For now this system does not detect the disconnection of an user. It should retrieve this info from dnsmasq (releases or state file?), or even better, hostapd (but then it gets only L2 info).
- This doesn't support IPv6.
