# coding: utf-8
def l5():
    import pickle
    import requests
    resp = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
    data = pickle.loads(bytes(resp.text, "UTF-8"))
    for line_raw in data:
        line = ""
        for chars in line_raw:
            line += chars[0]*chars[1]
        print(line)
