def l1(text=(
    "g fmn==c wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
    " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq r cvr gq qm jmle."
    " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    ): 
        translated = '' 
        for char in text: 
            try: 
                index = string.ascii_lowercase.index(char) 
                if index + 2 >= 26: 
                    index -= 26 
                translated += string.ascii_lowercase[index+2] 
            except ValueError: 
                translated += char 
        return translated
