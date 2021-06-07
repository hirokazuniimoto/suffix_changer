def get_suffix_pattern():
    #拡張子リスト
    sp = ['.txt','.html','.py','.c','.go','.conf','.md','.mod','.sum','.js','.css','.php','.cpp','.png','.xyz']
    return sp


def change_suffix(file_name, from_suffix, to_suffix):
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


def find_file_and_dir(dir_path):
    #files = glob.glob("./tmp/*")
    files = glob.glob(dir_path)
    for file in files:
        if '.' in file:
            result_files.append(file)
        else:
            find_file_and_dir(file+"/*")
    return result_files

def windowsPATH_to_linux(path):
    new_path = path.replace('\\','/')
    return new_path

def AA_print():
    welcomeAA = '''

    #    # ###### #       ####   ####  #    # ######
    #    # #      #      #    # #    # ##  ## #
    #    # #####  #      #      #    # # ## # #####
    # ## # #      #      #      #    # #    # #
    ##  ## #      #      #    # #    # #    # #
    #    # ###### ######  ####   ####  #    # ######

    '''

    toAA = '''
    #####  ####
      #   #    #
      #   #    #
      #   #    #
      #   #    #
      #    ####
    '''

    nameAA = '''
    ####  #    # ###### ###### ###### # #    #     ####  #    #   ##   #    #  ####  ###### #####
   #      #    # #      #      #      #  #  #     #    # #    #  #  #  ##   # #    # #      #    #
    ####  #    # #####  #####  #####  #   ##      #      ###### #    # # #  # #      #####  #    #
        # #    # #      #      #      #   ##      #      #    # ###### #  # # #  ### #      #####
   #    # #    # #      #      #      #  #  #     #    # #    # #    # #   ## #    # #      #   #
    ####   ####  #      #      #      # #    #     ####  #    # #    # #    #  ####  ###### #    #
    '''


    #AAの出力
    print(Fore.RED + welcomeAA)

    print(Fore.RED + toAA)

    print(Fore.RED + nameAA)

    #カラーをリセット
    print(Style.RESET_ALL)
    print("\n\n\n\n\n\n")
