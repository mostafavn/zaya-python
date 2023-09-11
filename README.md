

``zaya`` is a toolbox for the https://zaya.io community.


Install
-------

    pip3 install zaya


Usage
-------------

    import zaya


Connect
-------------

    zaya.connect('YourToken')
    # https://zaya.io/developers/api


account details

    zaya.account()


urls

    zaya.create_url('url')
    zaya.all_url()
    zaya.detail_url(id)
    zaya.update_url(id, 'url')
    zaya.delete_url(id)


domains

    zaya.all_domain()
    zaya.create_domain('domain')
    zaya.details_domain(id)
    zaya.update_domain(id, 'domain')
    zaya.delete_domain(id)


subjects

    zaya.subjects()
    zaya.create_subject('name', 'red')
    zaya.details_subject(id)
    zaya.update_subject(id, 'subject')
    zaya.delete_subject(id)


stats

    zaya.clicks(id)
    zaya.stats(id)
    zaya.referrers(id)
    zaya.countries(id)
    zaya.languages(id)
    zaya.browsers(id)
    zaya.devices(id)
    zaya.os(id)


get Information from zaya
-------

    zaya.__version__
    zaya.__author__
    zaya.__website__
    zaya.__documentation__