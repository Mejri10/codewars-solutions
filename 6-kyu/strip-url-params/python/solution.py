import re

def strip_url_params(url, params_to_strip = []):
    params = re.findall(r"(\w+)=(\w+)", url)
    if params:
        domain = url.split('?')[0]
        query = []
        param = []
        for name, value in params:
            if name not in param + params_to_strip:
                query.append("{}={}".format(name, value))
                param.append(name)
        query = '?' + '&'.join(query) 
        return domain + query
    else:
        return url
    
    