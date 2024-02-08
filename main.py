import gspread
from google.oauth2.service_account import Credentials

# 認証情報ファイルのパス
creds_file = './gcp_raspi_key.json'

# 認証情報を設定
creds = Credentials.from_service_account_file(creds_file, scopes=["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"])

# gspreadクライアントを初期化
client = gspread.authorize(creds)

# スプレッドシートを開く (スプレッドシート名またはスプレッドシートIDで指定)
spreadsheet = client.open("Raspi")

# 最初のワークシートを選択
worksheet = spreadsheet.sheet1

# A1セルに値を書き込む
worksheet.update_cell(1, 1, 'こんにちわ')

print("スプレッドシートに値を書き込みました。")
