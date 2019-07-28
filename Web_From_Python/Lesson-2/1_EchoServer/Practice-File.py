#Test file

"""
Understanding queries and URL quoting!
"""
from urllib.parse import urlparse, parse_qs

address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)

"""
Remeber that parse_qs() returns a dictionary of lists contianing all of the 
values associated with it! In this case, 
{'texture': ['fuzzy'], 'animal': ['gray squirrel']}
"""
query = parse_qs('texture=fuzzy&animal=gray+squirrel')
print(query)
# RETURNS: {'texture': ['fuzzy'], 'animal': ['gray squirrel']}
