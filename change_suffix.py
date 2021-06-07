#python3
#
#this is main progamm of suffix changer
#
# 2021/06/08
# author hirokazu niimoto

import pathlib
import shutil
import sys
import os
import time

#色付けライブラリ（Windows初期化）
from colorama import init
init()
#色付けライブラリ
from colorama import Fore, Back, Style

#Progress Bar
import tqdm
from tqdm import tqdm

##
#プログラムライブラリ
from lib import aa_print
from lib import windowsPATH_to_linux
from lib import core

result_files = [];


#メイン関数　
def main():
    welcome = aa_print.AA_PRINT()
    welcome.AA_print()

    try:
        path_create = windowsPATH_to_linux.WindowPATH_to_linux(sys.argv[1])
        new_path = path_create.windowsPATH_to_linux()
    except Exception as e:
        print('   ' + Fore.YELLOW + 'エラーです。' + Style.RESET_ALL + 'パスを入力してください。')
        exit()

    to_suffix = input('  First, which suffix do you want? (not include ".") :')

    while 1:
        print('  OK, this programm change the file suffix in ' + Fore.YELLOW + sys.argv[1] + Style.RESET_ALL + ' directory to ".' + Fore.BLUE  + to_suffix + Style.RESET_ALL +'".'  )
        flag = input('  please type yes(y)/no(n) :')

        if flag == 'yes' or flag == 'y':
            break
        elif flag == 'no' or flag == 'n':
            exit()

    print('\n\n')

    search_path =new_path + "/*"
    new_path = search_path

    suffix_change = core.Change_Suffix()

    result_files = [];
    result_files = suffix_change.find_file_and_dir(new_path,result_files)
    sp = suffix_change.get_suffix_pattern()
    to_suffix = '.' + to_suffix

    for file in tqdm(result_files):
        for s in sp:
            suffix_change.change_suffix(file,s,to_suffix)
            #a=1
            time.sleep(0.01)

    # NOTE: プログレスバーの使い方　tqdmの中のリストが普通に取り出される
    #a=0
    #for i in tqdm(range(1001)):
      #time.sleep(0.0001)
      #a+=i

    print('\n\n')
    print('   ' + Fore.GREEN + 'SUCCESS! MISSION COMPLETE!')



if __name__ == '__main__':
    main()
