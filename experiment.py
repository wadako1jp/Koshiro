import random
import os
import PyPDF2


def selection(slc, path, file_path):
    merger = PyPDF2.PdfFileMerger()
    files = os.listdir(path)
    files_file = [f for f in files]
    cand = random.choice(files_file)
    slc.append(cand)
    Q = os.path.join(path, cand)
    merger.append(Q)
    os.chdir(file_path)
    return cand, Q, path


def file_validation(tmp):
    tmp_ok = []                # 数字から始まるファイル名を格納
    tmp_num = []               # その数字を格納
    for i in tmp:
        numb = []                   # ファイル頭にある数字を文字列で格納
        list_i = list(i)            # 配列化したものを入れる
        if str.isdecimal(list_i[0]):        # 配列の最初が数字である場合
            tmp_ok.append(i)                # オッケー配列にファイル名を入れる
            j = 0
            while j < len(list_i):              # i番目のファイル名について頭から数字であるかどうか判定して数字ならnumbに加えていく
                if not str.isdecimal(list_i[j]):
                    break                           # 数字でないものが出てきたらbreak
                numb.append(list_i[j])
                j += 1
        m = ""
        for n in numb:                              # numbに入ってるstr型の数字についてそれらをつなげてintにする
            if str.isdecimal(n):
                m += n
                print(m)
                ll= int(m)
        if m != '':                                 # mが空でない場合tmp_numに入れる
            tmp_num.append(ll)
    print(tmp_ok)
    print(tmp_num)
    files = sorting(tmp_ok, tmp_num)
    return files


def sorting(a, b):
    c = []                                  # bの中身を小さい順に整列したしたあとの元のindexを配列化 (Ex:[10,1,9]の場合[1,2,0])
    d = []                                  # 返す配列
    for i in range(len(b)):
        c.append(b.index(min(b)))           # bの最小値のindexをcに入れる
        b[b.index(min(b))] += max(b)        # bの最小値に最大値を足して、forが回っている間に再度検出されないよう退避にする
    for j in range(len(a)):
        d.append(a[c[j]])                   # 返す配列に
    print(d)
    return d
