import PyPDF2
from distutils import dir_util
from pathlib import Path
import random
import os
import shutil

#前半の選択
slc1 = []
#後半の選択
slc2 = []

#入力フォームから、４つの選択問題を選ぶ
def input_form1(curr,file_path):
    print(os.listdir(curr))
    print(os.listdir(file_path))
    print("選択問題を4つ入力してください（EX:2,3,4,5）:")
    print("2.ハードウェア\n",
        "3.ソフトウェア\n",
        "4.データベース\n",
        "5.ネットワーク\n",
        "6.PM・サービスマネジメント\n",
        "7.ソフトウェア設計(21問)\n",
        "8.システム戦略・経営戦略\n",
        "--------------------------------------\n", end=" ")
    slc1 = input()
    slc1 = slc1.split(",")
    if len(slc1) > 5:
        print("選択問題が多いです。")
        input_form1(curr,file_path)
    if len(slc1) < 4:
        print("選択問題が少ないです。")
        input_form1(curr,file_path)
    select_1(slc1,file_path)
    input_form2(curr,file_path)


def input_form2(curr,file_path):

    print("選択問題を１つ選んでください:\n",
        "9.C\n",
        "10.Cobol\n",
        "11.java\n",
        "12.assenmbler\n",
        "13.Excel\n",
        "--------------------------------------\n", end=" ")
    slc2 = input()
    if len(slc2) != 1:
        ("問題を選択しなおしてください")
        input_form2(curr,file_path)
    if len(slc2) != 9 or 10 or 11 or 12 or 13:
        ("問題を選択しなおしてください")
        input_form2(curr,file_path)
    return slc2

def select_1 (slc1,file_path):
    base = file_path
    erab = []
    result_path =  os.path.join(file_path,"result")
    for i in slc1:
        if i == "2":
            #2のファイルを取ってくる。
            ein = os.path.join(file_path,"2_hardware")
            files = os.listdir(ein)
            files_file = [f for f in files]
            cand1=random.choice(files_file)
            erab.append(cand1)
            print(ein)
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "3":
            #3のファイルを取ってくる。
            zwei = os.path.join(file_path,"2_software")
            files = os.listdir(zwei)
            files_file = [f for f in files]
            cand2=random.choice(files_file)
            erab.append(cand2)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "4":
            #4のファイルを取ってくる。
            trei=os.path.join(file_path,"3_database")
            files = os.listdir(trei)
            files_file = [f for f in files]
            cand3=random.choice(files_file)
            erab.append(cand3)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "5":
            #5のファイルを取ってくる。
            fier=os.path.join(file_path,"4_network")
            files = os.listdir(fier)
            files_file = [f for f in files]
            cand4=random.choice(files_file)
            erab.append(cand4)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "6":
            #7のファイルを取ってくる。
            funf=os.path.join(file_path,"6_PM")
            files = os.listdir(funf)
            files_file = [f for f in files]
            cand5=random.choice(files_file)
            erab.append(cand5)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "7":
            #6のファイルを取ってくる。
            sechs=os.path.join(file_path,"5_soft_str")
            files = os.listdir(sechs)
            files_file =[f for f in files]
            cand6=random.choice(files_file)
            erab.append(cand6)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
        if i == "8":
            #8のファイルを取ってくる。
            sieben=os.path.join(file_path,"7_sys_str")
            files = os.listdir(sieben)
            files_file = [f for f in files]
            cand6=random.choice(files_file)
            erab.append(cand6)
            print(os.getcwd())
            shutil.copyfile((os.path.basename(__file__)),result_path)
            os.path.join(os.getcwd(),os.path.pardir)
    print(erab)
    write_file = "sumed.pdf"

    #移動

    #挿入

# def main(slc1, slc2):
#     write_file = "sumed.pdf"
#     write_path = os.path.join(os.getcwd(), "99_python実践", write_file)

#     merger = PyPDF2.PdfFileMerger()

#     merger.append(pdf1, pages=PyPDF2.pagerange.PageRange("5:8"))
#     merger.append(pdf2, pages=PyPDF2.pagerange.PageRange("4:8"))

#     merger.write(write_path)
#     merger.close()

if __name__ == "__main__":
    curr_path = os.getcwd()
    curr_path = os.path.join(curr_path, "99_python実践")
    file_path = os.path.join(curr_path, "python_pdf")
    print(file_path)
    input_form1(curr_path,file_path)
 
