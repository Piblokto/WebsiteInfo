import sys
from nslookup import Nslookup
import ipinfo
website = sys.argv[1]
# Lookup DNS
dns_query = Nslookup(dns_servers=["1.1.1.1"])
ips_record = dns_query.dns_lookup(website)
ip_address = ips_record.answer[0]
print("IP Address: ", ip_address)

# Check IP Address
ip_info_key = '' #PUT IPINFO API KEY HERE
handler = ipinfo.getHandler(ip_info_key)
details = handler.getDetails(ip_address)
print(f"Location: {details.city}, {details.region}, {details.country}")
print(f"Host: {details.org}")
