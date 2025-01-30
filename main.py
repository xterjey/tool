import subprocess
import time

# Konfigurasi RTMP
RTMP_URL = "rtmp://push-rtmp-l1-sg01.tiktokcdn.com/game"  # Ganti dengan RTMP URL Anda
STREAM_KEY = "stream-2134260430939095132?c=ID&keeptime=00093a80&wsSecret=371cd8b7525211acf549f5deb60d6b30&wsTime=679aa379"  # Ganti dengan Stream Key Anda
VIDEO_PATH = "1.mp4.mkv"  # Ganti dengan path ke video Anda

# Perintah ffmpeg untuk streaming dengan 2 CPU core
ffmpeg_command = [
    'ffmpeg',
    '-re',  # Membaca input pada kecepatan real-time
    '-stream_loop', '-1',  # Loop video tanpa batas
    '-i', VIDEO_PATH,  # Input video
    '-c:v', 'libx264',  # Codec video
    '-threads', '2',  # Menggunakan 2 CPU core
    '-preset', 'veryfast',  # Preset encoding
    '-maxrate', '6000k',  # Bitrate maksimum
    '-bufsize', '3000k',  # Buffer size
    '-vf', 'format=yuv420p',  # Format video
    '-c:a', 'aac',  # Codec audio
    '-b:a', '128k',  # Bitrate audio
    '-f', 'flv',  # Format output
    f'{RTMP_URL}/{STREAM_KEY}'  # URL RTMP lengkap
]

# Fungsi untuk menjalankan ffmpeg dengan restart otomatis
def run_ffmpeg():
    while True:
        try:
            print("Memulai streaming...")
            process = subprocess.run(ffmpeg_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Terjadi kesalahan saat streaming: {e}")
            print("Restarting FFmpeg in 5 seconds...")
            time.sleep(5)
        except KeyboardInterrupt:
            print("Streaming dihentikan oleh pengguna.")
            break

if __name__ == "__main__":
    run_ffmpeg()
