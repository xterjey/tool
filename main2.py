import subprocess
import time

# Meminta input dari pengguna
RTMP_URL = input("Masukkan RTMP URL: ")
STREAM_KEY = input("Masukkan Stream Key: ")
VIDEO_PATH = input("Masukkan path video: ")

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
