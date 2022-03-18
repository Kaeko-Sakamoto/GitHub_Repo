import SampleCode_DevA as A

nest_level = 1
tab             = "\t"*nest_level
this_mod_name   = "[Admin]"
next_mod        = A
next_mod_name   = next_mod.__name__

def initial():
    print(tab,this_mod_name, "initialメソッドが呼び出されました")
    ret_code = __call_other_module()
    print(tab,this_mod_name,"が完了しました")
    return ret_code

def __call_other_module():
    print(tab,this_mod_name, next_mod_name,"を呼び出します")
    #print(tab, "(",next_mod_name," は現在実装中) [TODO]")
    #ret_code = "[UC999] "+__name__+" failed."
    ret_code = next_mod.initial()
    return ret_code
