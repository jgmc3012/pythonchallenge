# coding: utf-8
def l3():
    import requests
    from re import findall
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    resp = requests.get(url)
    code = ''.join(resp.text.split('\n')[23:1272])
    chars = findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', ''.join(code))
    return ''.join(chars)
