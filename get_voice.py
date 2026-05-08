import yt_dlp
import os

# 這段程式碼會幫你把 YouTube 影片轉成 AI 聽得懂的 MP3
def download_nmixx_audio(url):
    print("正在準備下載 NMIXX 的聲音，請稍等...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # 檔案會存在這裡，名字叫 nmixx_voice.mp3
        'outtmpl': 'nmixx_voice.%(ext)s', 
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("---")
        print("成功了！你現在資料夾裡應該多了一個 nmixx_voice.mp3")
    except Exception as e:
        print(f"哎呀，出錯了：{e}")

# --- 這裡換成你想要的 NMIXX 影片網址 ---
video_url = "https://youtu.be/fg9Z4-Dnukk?si=Z9_b0mzIaU1Lng_X" 
download_nmixx_audio(video_url)