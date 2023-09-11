import requests

def connect(token):
    global header
    try:
        header = {'Content-Type':'Content-Type: application/x-www-form-urlencoded', 'Authorization': f'Authorization: Bearer {token}'}
    except:
        return 'The token is invalid,\nplease read the documentation https://pypi.org/project/zaya'
# _____________________________________________ account _____________________________________________

def account():
    try:
        req = requests.get(f"https://zaya.io/api/v1/account", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

# _____________________________________________ url _____________________________________________

def all_url():
    try:
        req = requests.get("https://zaya.io/api/v1/links", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def create_url(url):
    try:
        req = requests.post("https://zaya.io/api/v1/links", headers=header, params={'url':url})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def detail_url(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/links/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def update_url(id, url):
    try:
        req = requests.put(f"https://zaya.io/api/v1/links/{id}", headers=header, params={'url':url})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def delete_url(id):
    try:
        req = requests.delete(f"https://zaya.io/api/v1/links/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

# _____________________________________________ domains _____________________________________________

def all_domain():
    try:
        req = requests.get("https://zaya.io/api/v1/domains", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def create_domain(domain):
    try:
        req = requests.post("https://zaya.io/api/v1/domains", headers=header, params={'name':domain})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def details_domain(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/domains/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def update_domain(id, domain):
    try:
        req = requests.put(f"https://zaya.io/api/v1/domains/{id}", headers=header, params={'name':domain})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def delete_domain(id):
    try:
        req = requests.delete(f"https://zaya.io/api/v1/domains/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

# _____________________________________________ spaces _____________________________________________


def subjects():
    try:
        req = requests.get("https://zaya.io/api/v1/spaces", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def create_subject(name, color):
    try:
        req = requests.post("https://zaya.io/api/v1/spaces", headers=header, params={'name':name, 'color':color})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def details_subject(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/spaces/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def update_subject(id, name):
    try:
        req = requests.put(f"https://zaya.io/api/v1/spaces/{id}", headers=header, params={'name':name})
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def delete_subject(id):
    try:
        req = requests.delete(f"https://zaya.io/api/v1/spaces/{id}", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

# _____________________________________________ stats _____________________________________________

def stats(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/total", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def clicks(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/clicks", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def referrers(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/referrers", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def countries(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/countries", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def languages(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/languages", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def browsers(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/browsers", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def devices(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/devices", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'

def os(id):
    try:
        req = requests.get(f"https://zaya.io/api/v1/stats/{id}/operating-systems", headers=header)
        return req.json()
    except:
        return 'There is an error,\nplease read the documentation https://pypi.org/project/zaya'