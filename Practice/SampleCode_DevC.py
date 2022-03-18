

tab="\t"*4
this_mod_name="[DevC]"


def initial():
    print(tab,this_mod_name, this_mod_name, "が呼び出されました")
    ret_code = __end_edge()
    print(tab,this_mod_name, "が完了しました")
    return ret_code

def __end_edge():
    ret_code = "999"
    print(tab,this_mod_name, "処理終了。( RC=",ret_code,")")    

    return ret_code


