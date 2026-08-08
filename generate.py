import requests

def get_stream_url():
    # Menggunakan direct stream mono.ts dengan header referer resmi
    base_url = "https://qazaqstantv-stream.qazcdn.com/qazaqstantv/qazaqstantv/mono.ts.m3u8"
    headers = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36&Referer=https://player.rtrk.kz/&Origin=https://player.rtrk.kz"
    
    return base_url + headers

def main():
    m3u_lines = [
        "#EXTM3U",
        '#EXTINF:-1 group-title="Sports" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlr6LL8cZkMCiUYvyIXMyXT5VRfKVagiR3gS8oiNLg4A&s", Qazaqstan TV',
        get_stream_url()
    ]

    m3u_content = "\r\n".join(m3u_lines)

    # Simpan ke playlist.txt dan playlist.m3u
    with open("playlist.txt", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    print("[SUCCESS] Playlist Qazaqstan TV berhasil dibuat!")

if __name__ == "__main__":
    main()
