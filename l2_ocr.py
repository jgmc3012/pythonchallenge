# coding: utf-8
def l2():
    import requests
    from re import findall
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    resp = requests.get(url)
    code = ''.join(resp.text.split('\n')[37:1257])
    chars = findall('[a-zA-Z]+', ''.join(code))
    return ''.join(chars)
    
    
    
