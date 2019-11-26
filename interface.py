interface = 'Hardware is CSR vNIC, address is 0050.5602.415a (bia 0050.5602.415a)'
import re 
mac = re.search('0050.56.......',interface)
print 'There  is aa  seervice wwith oooii:'
print(mac.group(0))