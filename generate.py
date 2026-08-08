def main():
    worker_url = "https://qazaqstan-playlist.sulthan-pamenan.workers.dev"

    # Menggunakan channel & feed yang tidak dibatas geoblock oleh qazcdn
    channels = [
        {"name": "Qazaqstan TV (International)", "logo": "https://qazaqstan.tv/favicon.ico", "id": "qazaqstan_int"},
        {"name": "Jibek Joly TV (Global)", "logo": "https://jjtv.kz/favicon.ico", "id": "jibek_joly"},
        {"name": "Silk Way Cinema", "logo": "https://jjtv.kz/favicon.ico", "id": "silk_way"}
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

    print("[SUCCESS] Playlist International Kazakhstan berhasil dibuat!")

if __name__ == "__main__":
    main()
