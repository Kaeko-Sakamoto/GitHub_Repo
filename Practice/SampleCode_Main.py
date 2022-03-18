from telnetlib import RCP
import unittest
import SampleCode_Admin as Admin
import time

"""
    テスト対象のクラス名: import構文で指定した「SampleCode_Admin.py」を指定
"""
test_class_name = Admin


# Class definition
class TestSimple(unittest.TestCase):
    """
        テストドライバークラス:
        テスト用にクラス実行、メソッド実行の前後で必ず実行されるメソッドを定義し、
        各クラスやメソッドの挙動をコンソールに表示するテスト用のクラス
        標準クラスの"unittest"モジュールを利用しているため、特殊なサードパーティーモジュールをpipする必要がない点が特徴

        test_call_other()メソッドの中で、テストしたいクラスを呼び出すことで起動可能（クラス定義外で指定）
    """

    @classmethod
    def setUpClass(cls):
        """各クラスが実行される直前に一度だけ呼び出されるメソッド"""
#        target_class = "A"
        __target_class_name = test_class_name.__name__
        cls.__rc = ""

        print("[Main] メインクラス開始")
        print("[Main] setUpClass実行中.")
        print("[Main]",__target_class_name+"を呼び出す処理。クラス: 初期化完了 [", time.asctime( time.localtime(time.time()) ), "]"  )

    def setUp(self):
        """各テストメソッドが実行される直前に呼び出される"""
        print("[Main]","外部呼び出し: 呼び出し先=クラス名[", test_class_name.__name__,"]"  )

    def test_call_other(self):
        ret_code = test_class_name.initial()
        #print("[Main] リターンコード=", ret_code)
        self.__rc=ret_code

    def tearDown(self):
        """各テストメソッドが実行された直後に呼び出される"""
        if self.__rc == "000":
            print("[Main] 成功！！")
        else:
            print("[Main] 失敗！！ リターンコード＝", self.__rc)


#------------------------------------------------------------------------------
# Main module
#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()






