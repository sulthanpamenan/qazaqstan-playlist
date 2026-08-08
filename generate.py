def main():
    # Masukkan URL Worker Cloudflare milikmu di sini
    worker_url = "https://qazaqstan-playlist.sulthanpamenan.workers.dev" # <-- SESUAIKAN DENGAN URL WORKER KAMU

    channels = [
        {"name": "Qazaqstan TV (National)", "logo": "https://qazaqstan.tv/favicon.ico", "id": "qazaqstan"},
        {"name": "Qazaqstan TV (International)", "logo": "https://qazaqstan.tv/favicon.ico", "id": "qazaqstan_int"},
        {"name": "QazSport TV", "logo": "https://qazsport.tv/favicon.ico", "id": "qazsport"},
        {"name": "Balapan TV", "logo": "https://balapan.tv/favicon.ico", "id": "balapan"},
        {"name": "El Arna TV", "logo": "https://elarna.tv/favicon.ico", "id": "elarna"}
    ]

    m3u_lines = ["#EXTM3U"]

    for ch in channels:
        m3u_lines.append(f'#EXTINF:-1 group-title="Kazakhstan" tvg-logo="{ch["logo"]}", {ch["name"]}')
        m3u_lines.append(f'{worker_url}/?ch={ch["id"]}')

    m3u_content = "\r\n".join(m3u_lines)

    with open("playlist.txt", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    print("[SUCCESS] Playlist All Kazakhstan Channels berhasil dibuat!")

if __name__ == "__main__":
    main()
