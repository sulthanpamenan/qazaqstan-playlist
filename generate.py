def main():
    # Masukkan URL Cloudflare Worker milikmu di sini
    proxy_url = "https://qazaqstan-playlist.sulthan-pamenan.workers.dev/"  # <-- GANTI DENGAN LINK WORKER KAMU

    m3u_lines = [
        "#EXTM3U",
        '#EXTINF:-1 group-title="Sports" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlr6LL8cZkMCiUYvyIXMyXT5VRfKVagiR3gS8oiNLg4A&s", Qazaqstan TV',
        proxy_url
    ]

    m3u_content = "\r\n".join(m3u_lines)

    with open("playlist.txt", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    print("[SUCCESS] Playlist Qazaqstan via Cloudflare Proxy berhasil dibuat!")

if __name__ == "__main__":
    main()
