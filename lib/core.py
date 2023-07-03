#python3
#
#this is core progamm of suffix changer
#
# 2021/06/08
# author hirokazu niimoto


#ディレクトリ内のファイル名を表示するライブラリ
import glob
import os
import pathlib
import shutil
import sys
import os
import time


class Change_Suffix(object):
    """docstring forChange_Suffix."""

    def get_suffix_pattern(self):
        #拡張子リスト
        sp = ['.db','.txt','.html','.py','.c','.go','.conf','.md','.mod','.sum','.js','.css','.php','.cpp','.png','.xyz']
        return sp

    def change_suffix(self,file_name, from_suffix, to_suffix):
        # ファイルの拡張子を得る
        sf = pathlib.PurePath(file_name).suffix

        # 変更対象かどうか判定する
        if sf == from_suffix:
            # ファイル名(拡張子除く)を得る
            st = pathlib.PurePath(file_name).stem
            dirname = os.path.dirname(file_name)

            st = dirname + '/' + st

            # 変更後のファイル名を得る
            to_name = st + to_suffix

            # ファイル名を変更する
            shutil.move(file_name, to_name)


    def find_file_and_dir(self,dir_path,result_files):
        #files = glob.glob("./tmp/*")
        files = glob.glob(dir_path)
        for file in files:
            if '.' in file:
                result_files.append(file)
            else:
                self.find_file_and_dir(file+"/*",result_files)
        return result_files
