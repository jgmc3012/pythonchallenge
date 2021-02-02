# coding: utf-8
def l4(number=12345):
    import requests
    from re import search
    for i in range(400):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}"
        resp = requests.get(url)
        match = search("next nothing is (\d+)", resp.text)
        if not match:
            return {"number":number, "text":resp.text, 'i':i}
        number = match.groups()[0]
        if i % 10 == 0:
            print("vamor por el", i+1)
    return {"number":number, "text":resp.text, 'i':i} 
