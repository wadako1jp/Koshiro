import PyPDF2
import random
import os
# import experiment.py

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

    zero = os.path.join(file_path, "1_security")
    files = os.listdir(zero)
    files_file = [f for f in files]
    cand = random.choice(files_file)
    slc.append(cand)
    Q = os.path.join(zero, cand)
    merger.append(Q)
    os.chdir(file_path)

    for i in erab1:
        if i == "2":
            # 2のファイルを取ってくる。
            ein = os.path.join(file_path, "2_hardware")
            files = os.listdir(ein)
            files_file = [f for f in files]
            cand1 = random.choice(files_file)
            slc.append(cand1)
            Q1 = os.path.join(ein, cand1)
            merger.append(Q1)
            os.chdir(file_path)
        if i == "3":
            # 3のファイルを取ってくる。
            zwei = os.path.join(file_path, "2_software")
            files = os.listdir(zwei)
            files_file = [f for f in files]
            cand2 = random.choice(files_file)
            slc.append(cand2)
            Q2 = os.path.join(zwei, cand2)
            merger.append(Q2)
            os.chdir(file_path)
        if i == "4":
            # 4のファイルを取ってくる。
            trei = os.path.join(file_path, "3_database")
            files = os.listdir(trei)
            files_file = [f for f in files]
            cand3 = random.choice(files_file)
            slc.append(cand3)
            Q3 = os.path.join(trei, cand3)
            merger.append(Q3)
            os.chdir(file_path)
        if i == "5":
            # 5のファイルを取ってくる。
            fier = os.path.join(file_path, "4_network")
            files = os.listdir(fier)
            files_file = [f for f in files]
            cand4 = random.choice(files_file)
            slc.append(cand4)
            Q4 = os.path.join(fier, cand4)
            merger.append(Q4)
            os.chdir(file_path)
        if i == "6":
            # 7のファイルを取ってくる。
            funf = os.path.join(file_path, "6_PM")
            files = os.listdir(funf)
            files_file = [f for f in files]
            cand5 = random.choice(files_file)
            slc.append(cand5)
            Q5 = os.path.join(funf, cand5)
            merger.append(Q5)
            os.chdir(file_path)
        if i == "7":
            # 6のファイルを取ってくる。
            sechs = os.path.join(file_path, "5_soft_str")
            files = os.listdir(sechs)
            files_file = [f for f in files]
            cand6 = random.choice(files_file)
            slc.append(cand6)
            Q6 = os.path.join(sechs, cand6)
            merger.append(Q6)
            os.chdir(file_path)
        if i == "8":
            # 8のファイルを取ってくる。
            sieben = os.path.join(file_path, "7_sys_str")
            files = os.listdir(sieben)
            files_file = [f for f in files]
            cand7 = random.choice(files_file)
            slc.append(cand7)
            Q7 = os.path.join(sieben, cand7)
            merger.append(Q7)
            os.chdir(file_path)

    acht = os.path.join(file_path, "8_algo")
    files = os.listdir(acht)
    files_file = [f for f in files]
    cand8 = random.choice(files_file)
    slc.append(cand8)
    Q8 = os.path.join(acht, cand8)
    merger.append(Q8)
    os.chdir(file_path)

    # リストとして保持している
    if erab2 == "9":
        # 2のファイルを取ってくる。
        neun = os.path.join(file_path, "9_C")
        files = os.listdir(neun)
        files_file = [f for f in files]
        cand9 = random.choice(files_file)
        slc.append(cand9)
        Q9 = os.path.join(neun, cand9)
        merger.append(Q9)
        os.chdir(file_path)
    if erab2 == "10":
        # 3のファイルを取ってくる。
        zhen = os.path.join(file_path, "10_cobol")
        files = os.listdir(zhen)
        files_file = [f for f in files]
        cand10 = random.choice(files_file)
        slc.append(cand10)
        Q10 = os.path.join(zhen, cand10)
        merger.append(Q10)
        os.chdir(file_path)
    if erab2 == "11":
        # 4のファイルを取ってくる。
        elf = os.path.join(file_path, "11_java")
        files = os.listdir(elf)
        files_file = [f for f in files]
        cand11 = random.choice(files_file)
        slc.append(cand11)
        Q11 = os.path.join(elf, cand11)
        merger.append(Q11)
        os.chdir(file_path)
    if erab2 == "12":
        # 2のファイルを取ってくる。
        zwolf = os.path.join(file_path, "12_assembler")
        files = os.listdir(zwolf)
        files_file = [f for f in files]
        cand12 = random.choice(files_file)
        slc.append(cand12)
        Q12 = os.path.join(zwolf, cand12)
        merger.append(Q12)
        os.chdir(file_path)
    if erab2 == "13":
        # 3のファイルを取ってくる。
        treizehn = os.path.join(file_path, "13_Excel")
        files = os.listdir(treizehn)
        files_file = [f for f in files]
        cand13 = random.choice(files_file)
        slc.append(cand13)
        print(type(cand13))
        Q13 = os.path.join(treizehn, cand13)
        merger.append(Q13)
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
