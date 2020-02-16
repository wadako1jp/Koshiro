import PyPDF2
import random
import os
from experiment import selection

# 前半の選択
slc = []
# 後半の選択
slc2 = []

result_path = os.path.join(os.getcwd(), "result")

dict_all ={
"1_security": 1,
"2_hardware" : 2,
"2_software": 3,
"3_database": 4,
"4_network": 5,
"6_PM": 6,
"5_soft_str": 7,
"7_sys_str": 8,
"9_C": 9,
"10_cobol": 10,
"11_java": 11,
"12_assembler": 12,
"13_excel": 13}


# slc1とslc2の初期化
def __init__():
    i = 0
    j = 0
    while(i < 100):
        slc1.append(0)
    while(j < 100):
        slc1.append(0)


# 入力フォームから、４つの選択問題を選ぶ
def input_form1(curr, file_path):
    """
    Parameters
    ------
    name : str
        名前

    Returns
    ------
        Hello! とnameの結合結果
    """

    global slc1
    global slc2

    print("選択問題を4つ入力してください（記入例:2,3,4,5）:\n")
    print("2.ハードウェア")
    print("3.ソフトウェア")
    print("4.データベース")
    print("5.ネットワーク")
    print("6.PM・サービスマネジメント")
    print("7.ソフトウェア設計(21問)")
    print("8.システム戦略・経営戦略")
    print("-------------------------------")
    erab1 = input("Put 4: ")
    erab1 = erab1.split(",")
    if len(erab1) > 5:
        print("\n\n選択問題が多いです。\n\n")
        input_form1(curr, file_path)
    if len(erab1) < 4:
        print("\n\n選択問題が少ないです。\n\n")

    print("選択問題を１つ選んでください:\n9.C\n10.Cobol\n11.java\n12.assenmbler\n13.Excel")
    print("-----------------------------")
    erab2 = input("Choose 1: ")
    if len(erab2) == 0:
        print("問題を選択しなおしてください")
        input_form1(curr, file_path)
    else:
        select_1(erab1, erab2, file_path, curr)


def select_1(erab1, erab2, file_path, curr):
    """
    ここに函数の説明（どのような処理を行うものかを記述する）

    Parameters
    ------
    name : str
        名前

    Returns
    ------
        Hello! とnameの結合結果
    """

    global slc
    global slc2
    global result_path
    merger = PyPDF2.PdfFileMerger()

    erab1.append(erab2)
    print("erab1 goes like >>>", erab1)

    path = os.path.join(file_path, "1_security")
    files = os.listdir(path)
    selection(slc, files, path)
    merger.append(Q)
    os.chdir(file_path)

    for i in erab1:
        if i == "2":
            # 2のファイルを取ってくる。
            path = os.path.join(file_path, "2_hardware")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "3":
            # 3のファイルを取ってくる。
            path = os.path.join(file_path, "2_software")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "4":
            # 4のファイルを取ってくる。
            path = os.path.join(file_path, "3_database")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "5":
            # 5のファイルを取ってくる。
            path = os.path.join(file_path, "4_network")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "6":
            # 7のファイルを取ってくる。
            path = os.path.join(file_path, "6_PM")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "7":
            # 6のファイルを取ってくる。
            path = os.path.join(file_path, "5_soft_str")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)
        if i == "8":
            # 8のファイルを取ってくる。
            path = os.path.join(file_path, "7_sys_str")
            files = os.listdir(path)
            selection(slc, files, path)
            merger.append(Q)
            os.chdir(file_path)

    path = os.path.join(file_path, "8_algo")
    files = os.listdir(path)
    selection(slc, files, path)
    merger.append(Q)
    os.chdir(file_path)

    # リストとして保持している
    if erab2 == "9":
        # 2のファイルを取ってくる。
        path = os.path.join(file_path, "9_C")
        files = os.listdir(path)
        selection(slc, files, path)
        merger.append(Q)
        os.chdir(file_path)
    if erab2 == "10":
        # 3のファイルを取ってくる。
        path = os.path.join(file_path, "10_cobol")
        files = os.listdir(path)
        selection(slc, files, path)
        os.chdir(file_path)
    if erab2 == "11":
        # 4のファイルを取ってくる。
        path = os.path.join(file_path, "11_java")
        files = os.listdir(path)
        selection(slc, files, path)
        merger.append(Q)
        os.chdir(file_path)
    if erab2 == "12":
        # 2のファイルを取ってくる。
        path = os.path.join(file_path, "12_assembler")
        files = os.listdir(path)
        selection(slc, files, path)
        merger.append(Q)
        os.chdir(file_path)
    if erab2 == "13":
        # 3のファイルを取ってくる。
        path = os.path.join(file_path, "13_Excel")
        files = os.listdir(path)
        selection(slc, files, path)
        merger.append(Q)
        os.chdir(file_path)

    # 最後にPDFのアプリ起動させたら嬉しくない？

    merger = PyPDF2.PdfFileMerger()
    result_final = os.path.join(result_path, "result.pdf")
    # resultファイルは
    merger.write(result_final)
    merger.close()

    print("今回は、", str([slc]), "の問題です")
    print("resultフォルダにあるresult.pdfをみてください")
    print("終了\n")
    exit


if __name__ == "__main__":
    curr_path = os.getcwd()
    curr_path = os.path.join(curr_path)
    file_path = os.path.join(curr_path)
    print(file_path)
    input_form1(curr_path, file_path)
