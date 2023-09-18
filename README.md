# Zaya library for Python
using this package you can easily implement the [Zaya](https://zaya.io) link shortener in your python project.

> First you need to get your API token from [Zaya](https://zaya.io/developers/api)


### Installation
```py
pip3 install zaya
```

### Initial construction
```py
import zaya
zaya.connect('YourToken')
```

### Account details
```py
zaya.account()
```

### Urls
```py
zaya.create_url('url')
zaya.all_url()
zaya.detail_url(id)
zaya.update_url(id, 'url')
zaya.delete_url(id)
```

### Domains
```py
zaya.all_domain()
zaya.create_domain('domain')
zaya.details_domain(id)
zaya.update_domain(id, 'domain')
zaya.delete_domain(id)
```

### Subjects
```py
zaya.subjects()
zaya.create_subject('name', 'red')
zaya.details_subject(id)
zaya.update_subject(id, 'subject')
zaya.delete_subject(id)
```

### Stats
```py
zaya.clicks(id)
zaya.stats(id)
zaya.referrers(id)
zaya.countries(id)
zaya.languages(id)
zaya.browsers(id)
zaya.devices(id)
zaya.os(id)
```

### Getting package information
```py
zaya.__version__
zaya.__author__
zaya.__website__
zaya.__documentation__
```
