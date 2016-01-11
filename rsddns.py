import pyrax
import urllib3

rsUser = ""
rsKey = ""
domainName = ""
subdomain = ""

response = urllib2.urlopen('http://ipv4.icanhazip.com')
ip = response.read().strip()

pyrax.set_setting('identity_type', 'rackspace')
pyrax.set_credentials(rsUser, rsKey)

domain = pyrax.cloud_dns.find(name = domainName)
record = domain.find_record('A', name = subdomain + "." + domainName)

record.update(data = ip)