
"""
    プログラムの注意点
    ⓵フォルダ構成は「99_python実践」以下は触らないでください。このフォルダ構成ではないと動きません。
    ⓶問13と問8の順番が逆です。

    メンテナンス
    *もし新しいファイルを更新場合は、フォルダpython_pdf下にある各大問フォルダに以下の手順で記載してください。
    1.問題から大問毎にpdfを分割
    2.フォルダの名前にそろえて格納。
    格納する大問のフォルダを誤った場合、誤ったファイルが分割して組み込まれることになるので、更新したときはDocStreamに、
    「更新したファイルの年度、もしくはファイル名」を記載してください。

    更新履歴
    (更新者、更新したファイルの年度もしくはファイル名、更新年度）
    -----------------------------------------




"""

import PyPDF2
import os
import subprocess
from experiment import selection
from experiment import file_validation
from experiment import sorting

CURR_PATH = os.getcwd()
CURR_PATH = os.path.join(CURR_PATH, "99_PYTHON実践")
FILE_PATH = os.path.join(CURR_PATH, "PYTHON_PDF")

# 前半の選択
slc = []

result_path = os.path.join(os.getcwd(), "99_python実践", "result")

# slc1とslc2の初期化
def __init__():
    i = 0
    j = 0
    while(i < 100):
        slc.append(0)

# 入力フォームから、４つの選択問題を選ぶ
def input_form1(curr, file_path):
    """

    最初の入力フォームです。
    選択項目が２つあり、入力フォームを２つ用意しています。
    erab1に4つの要素を格納しています
    erab2に1個の要素を格納しています

    パラメータ
    Curr・・・現在のパス
    file_path・・・問題が格納されているフォルダへのパス
    ------
    name : str
        名前
    Returns erab1,erab2
    ------
    erab1・・・前半の４つの選択問題をリストとして保持しています
    erab2・・・後半の１つの選択問題をリストとして保持しています
    """
    #erab1の選択画面
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
    #異常系の排除
    if len(erab1) > 5:
        print("\n\n選択問題が多いです。\n\n")
        input_form1(curr, file_path)
    if len(erab1) < 4:
        print("\n\n選択問題が少ないです。\n\n")
        input_form1(curr, file_path)
    #erab2の選択画面
    print("選択問題を１つ選んでください:\n9.C\n10.Cobol\n11.java\n12.assenmbler\n13.Excel")
    print("-----------------------------")
    erab2 = input("Choose 1: ")
    #異常系の排除
    if len(erab2) == 0:
        print("問題を選択しなおしてください")
        input_form1(curr, file_path)
    else:
        select_1(erab1, erab2, file_path, curr)

def select_1(erab1, erab2, file_path, curr):
    """
    選択した問題をerab1にまとめて格納して、
    それを引数として、python_pdfのファイルをランダムに取り出しています。
    なお問題をランダムに取り出す処理は、外部ファイルのselectionで行っています。
    パスの名前は外部ファイルのvalidation_fileで行っています。

    パラメータ
    Curr・・・現在のパス
    file_path・・・問題が格納されているフォルダへのパス
    erab1・・・前半の４つの選択問題をリストとして保持しています
    erab2・・・後半の１つの選択問題をリストとして保持しています
    ------
        函数:select_1
    Return result.pdf
    ------
    """
    #初期条件を整理しています
    global slc
    global result_path
    merger = PyPDF2.PdfFileMerger()
    Qs = []
    #erab1,erab2をerab1に統合しています
    erab1.append(erab2)
    #フォルダpython_pdfに存在するフォルダのリストを表示しています
    tmp = os.listdir(file_path)
    file_validation(tmp)
    #tmpに格納されているフォルダのリストを整理して返してくるようにしています
    list_files = file_validation(tmp)
    select_q = []
    #整理されたlist_filesを使って、erab1のリストを読み込みます。
    #ここでランダム選択した問題をリストslcに格納してあります。
    path = os.path.join(file_path, list_files[0])
    cand, Q, path=selection(slc, path, file_path)
    #Qには選択された問題へのパスが格納されているので、それをQsにappendします。
    select_q.append(cand)
    Qs.append(Q)
    os.chdir(file_path)
    #erab1のリスト内を精査します。
    for i in erab1:
        n=int(i)
        #リストに格納されているのは2~14なので、それに対応する大問から問題をもってくる。
        for a in range(2,14):
            if a == n:
                path = os.path.join(file_path, list_files[a])
                cand, Q, path=selection(slc, path, file_path)
                select_q.append(cand)
                Qs.append(Q)
                os.chdir(file_path)
            else:
                pass

    path = os.path.join(file_path, list_files[8])
    cand, Q, path=selection(slc, path, file_path)
    select_q.append(cand)
    Qs.append(Q)
    os.chdir(file_path)

    merger = PyPDF2.PdfFileMerger()
    #Qsに格納されているパスを使って、merger.appendしていきます
    for k in Qs:
        merger.append(k)
    #書き込むファイルのパスを指定します
    result_final = os.path.join(curr_path, "result", "result.pdf")
    #appendされた内容を指定されたパス（変数result_final）に書き込みます。
    #result_pdfを閉じていないとここで「invalid argument」が出ます。
    merger.write(result_final)
    merger.close()

    #slcには選択した問題のファイル名がかきこまれています。
    print("\n\n今回は、", str([select_q]), "の問題です")
    print("PDFを統合しました\nresultフォルダにあるresult.pdfをみてください")
    print("終了\n")
    subprocess.Popen(result_final, shell=True)
    exit

#MAIN函数では、CURR_PATH（カレントパス）と、FILE_PATH（ファイルパス）指定してください。
