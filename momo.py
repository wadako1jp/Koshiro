import re
import sys

def get_phone_and_email(phone_regex,email_regex):
    # TODO: 電話番号の正規表現のコンパイル。
    phone = re.compile(phone_regex)
    # TODO: 電子メールの正規表現のコンパイル。
    email = re.compile(email_regex)
    # TODO: クリップボードのテキスト（電話番号、電子メール）を検索する。
    mail=email.search(pyperclip.copy)
    phone.search(pyperclip.copy)
    # TODO: 検索結果をクリップボードに貼り付ける。
    pyperclip.paste(email)
    pyperclip.paste(phone)

# テストコード
if __name__ == "__main__":
    phone_regex=r"\d{3}-\d{4}-\d{4}"
    email_regex=r"[\w-]+[\w]+@[\w.]+"
# ユーザー名@ドメイン名.co.jp
# ユーザー名は、「英数字（大文字または小文字）、_、-」で構成されている
# ドメイン名は、「英数字（大文字または小文字）」で構成されている
