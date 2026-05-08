import whisper
import csv # 新加入：處理表格的工具

print("正在讀取 AI 模型...")
model = whisper.load_model("base")

print("AI 開始聽 NMIXX 的聲音了...")
result = model.transcribe("nmixx_voice.mp3")

print("--- 辨識結果 ---")
# 1. 準備一個空的清單來存資料
data_rows = []

for segment in result['segments']:
    start = segment['start']
    text = segment['text']
    print(f"[{start:.2f}s]: {text}")
    # 把秒數和內容存進清單
    data_rows.append([f"{start:.2f}", text])

# 2. 【核心修改】把結果存成 CSV 表格檔
with open('nmixx_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['秒數', '內容']) # 寫入標題
    writer.writerows(data_rows)     # 寫入所有 AI 聽到的內容

# 原本存純文字檔的部分保留
with open("nmixx_script.txt", "w", encoding="utf-8") as f:
    f.write(result['text'])

print("---")
print("🎉 太棒了！現在你的資料夾多了一個 'nmixx_data.csv'")
print("這個檔案就是網頁字典的『大腦』！")