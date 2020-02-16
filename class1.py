import PyPDF2
import random
import os
import shutil

# 前半の選択
slc1 = []
# 後半の選択
slc2 = []


def __init__():
    i = 0
    j = 0
    while(i < 100):
        slc1.append(0)
    while(j < 100):
        slc1.append(0)


# 入力フォームから、４つの選択問題を選ぶ
def input_form1(curr, file_path):
    print("選択問題を4つ入力してください（EX:2,3,4,5）:\n")
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
        input_form1(curr, file_path)
    select_1(erab1, file_path, curr)


def select_1(erab1, file_path, curr):
    global slc1
    result_path = os.path.join(file_path, "result", "result.pdf")

    zero = os.path.join(file_path, "1_security")
    files = os.listdir(zero)
    files_file = [f for f in files]
    cand = random.choice(files_file)
    slc1.append(cand)
    Q = os.path.join(zero, cand)
    shutil.copyfile(Q, result_path)
    os.chdir(file_path)

    for i in erab1:
        if i == "2":
            # 2のファイルを取ってくる。
            ein = os.path.join(file_path, "2_hardware")
            files = os.listdir(ein)
            files_file = [f for f in files]
            cand1 = random.choice(files_file)
            slc1.append(cand1)
            Q1 = os.path.join(ein, cand1)
            shutil.copyfile(Q1, result_path)
            os.chdir(file_path)
        if i == "3":
            # 3のファイルを取ってくる。
            zwei = os.path.join(file_path, "2_software")
            files = os.listdir(zwei)
            files_file = [f for f in files]
            cand2 = random.choice(files_file)
            slc1.append(cand2)
            Q2 = os.path.join(zwei, cand2)
            shutil.copyfile(Q2, result_path)
            os.chdir(file_path)
        if i == "4":
            # 4のファイルを取ってくる。
            trei = os.path.join(file_path, "3_database")
            files = os.listdir(trei)
            files_file = [f for f in files]
            cand3 = random.choice(files_file)
            slc1.append(cand3)
            Q3 = os.path.join(trei, cand3)
            shutil.copyfile(Q3, result_path)
            os.chdir(file_path)
        if i == "5":
            # 5のファイルを取ってくる。
            fier = os.path.join(file_path, "4_network")
            files = os.listdir(fier)
            files_file = [f for f in files]
            cand4 = random.choice(files_file)
            slc1.append(cand4)
            Q4 = os.path.join(fier, cand4)
            shutil.copyfile(Q4, result_path)
            os.chdir(file_path)
        if i == "6":
            # 7のファイルを取ってくる。
            funf = os.path.join(file_path, "6_PM")
            files = os.listdir(funf)
            files_file = [f for f in files]
            cand5 = random.choice(files_file)
            slc1.append(cand5)
            Q5 = os.path.join(funf, cand5)
            shutil.copyfile(Q5, result_path)
            os.chdir(file_path)
        if i == "7":
            # 6のファイルを取ってくる。
            sechs = os.path.join(file_path, "5_soft_str")
            files = os.listdir(sechs)
            files_file = [f for f in files]
            cand6 = random.choice(files_file)
            slc1.append(cand6)
            Q6 = os.path.join(sechs, cand6)
            shutil.copyfile(Q6, result_path)
            os.chdir(file_path)
        if i == "8":
            # 8のファイルを取ってくる。
            sieben = os.path.join(file_path, "7_sys_str")
            files = os.listdir(sieben)
            files_file = [f for f in files]
            cand7 = random.choice(files_file)
            slc1.append(cand7)
            Q7 = os.path.join(sieben, cand7)
            shutil.copyfile(Q7, result_path)
            os.chdir(file_path)
    print(slc1)
    input_form2(curr, file_path)


def input_form2(curr, file_path):

    print("選択問題を１つ選んでください:\n9.C\n10.Cobol\n11.java\n12.assenmbler\n13.Excel")
    print("-----------------------------")
    erab2 = input("Choose 1: ")
    if len(erab2) == 0:
        print("問題を選択しなおしてください")
        input_form2(curr, file_path)
    else:
        select_form2(erab2, file_path)


def select_form2(erab2, file_path):
    global slc1
    global slc2
    result_path = os.path.join(file_path, "result", "result.pdf")

    acht = os.path.join(file_path, "8_algo")
    files = os.listdir(acht)
    files_file = [f for f in files]
    cand8 = random.choice(files_file)
    slc2.append(cand8)
    Q8 = os.path.join(acht, cand8)
    shutil.copyfile(Q8, result_path)
    os.chdir(file_path)

    if erab2 == "9":
        # 2のファイルを取ってくる。
        neun = os.path.join(file_path, "9_C")
        files = os.listdir(neun)
        files_file = [f for f in files]
        cand9 = random.choice(files_file)
        slc2.append(cand9)
        Q9 = os.path.join(neun, cand9)
        shutil.copyfile(Q9, result_path)
        os.chdir(file_path)
    if erab2 == "10":
        # 3のファイルを取ってくる。
        zhen = os.path.join(file_path, "10_cobol")
        files = os.listdir(zhen)
        files_file = [f for f in files]
        cand10 = random.choice(files_file)
        slc2.append(cand10)
        Q10 = os.path.join(zhen, cand10)
        shutil.copyfile(Q10, result_path)
        os.chdir(file_path)
    if erab2 == "11":
        # 4のファイルを取ってくる。
        elf = os.path.join(file_path, "11_java")
        files = os.listdir(elf)
        files_file = [f for f in files]
        cand11 = random.choice(files_file)
        slc2.append(cand11)
        Q11 = os.path.join(elf, cand11)
        shutil.copyfile(Q11, result_path)
        os.chdir(file_path)
    if erab2 == "12":
        # 2のファイルを取ってくる。
        zwolf = os.path.join(file_path, "12_assembler")
        files = os.listdir(zwolf)
        files_file = [f for f in files]
        cand12 = random.choice(files_file)
        slc2.append(cand12)
        Q12 = os.path.join(zwolf, cand12)
        shutil.copyfile(Q12, result_path)
        os.chdir(file_path)
    if erab2 == "13":
        # 3のファイルを取ってくる。
        treizehn = os.path.join(file_path, "13_excel")
        files = os.listdir(treizehn)
        files_file = [f for f in files]
        cand13 = random.choice(files_file)
        slc2.append(cand13)
        Q13 = os.path.join(treizehn, cand13)
        shutil.copyfile(Q13, result_path)
        os.chdir(file_path)

    # 最後にPDFのアプリ起動させたら嬉しくない？
    print("今回は、", str([slc1, slc2]), "の問題です")
    exit()


if __name__ == "__main__":
    curr_path = os.getcwd()
    curr_path = os.path.join(curr_path)
    file_path = os.path.join(curr_path)
    print(file_path)
    input_form1(curr_path, file_path)
