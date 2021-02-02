# coding: utf-8
def l6():
    import requests
    from zipfile import ZipFile
    from io import BytesIO
    from re import search
    filename = "90052.txt"
    resp = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip", stream=True)
    b_data = BytesIO(resp.content)
    message = ""
    with ZipFile(b_data) as myzip:
        while True:
            with myzip.open(filename, 'r') as myfile:
                text = myfile.read().decode()
                message += myzip.getinfo(filename).comment.decode()
                match = search("nothing is (\d+)", text)
                if not match:
                    return {"last_text":text, "last_filename":filename, "message": message}
                number = match.groups()[0]
                filename = number + ".txt"
                
print(l6()['message'])
