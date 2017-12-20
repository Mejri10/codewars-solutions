import re

def domain_name(url):
    return re.search(r"(w{3})?\.?([A-Za-z_-]+)\.", url).group(2)
    