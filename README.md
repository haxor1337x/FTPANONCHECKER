FTP Scanner
===========

Program ini akan memeriksa daftar FTP server yang diberikan oleh pengguna dan mengecek apakah anonymous FTP access diaktifkan atau tidak. Program ini menggunakan `ftplib` untuk terhubung ke server dan `concurrent.futures` untuk memeriksa setiap server secara asinkron. Program juga menggunakan `colorama` untuk memberikan output yang lebih menarik dan mudah dibaca.

Cara Penggunaan
---------------

1.  Clone repository ini atau unduh file `ftp_scanner.py`.
2.  Pastikan Python sudah terpasang di komputer Anda.
3.  Install library `ftplib`, `concurrent.futures`, dan `colorama` dengan perintah `pip install ftplib concurrent.futures colorama`.
4.  Buat file dengan daftar FTP server yang ingin diperiksa dan simpan dengan format `.txt`.
5.  Jalankan program dengan perintah `python gas.py`.
6.  Masukkan nama file dengan daftar FTP server yang ingin diperiksa.
7.  Tunggu program menyelesaikan prosesnya. Hasil akan ditampilkan di layar dan disimpan dalam file `ftpanon.txt`.

Semoga program ini bermanfaat untuk Anda. Jangan ragu untuk memberikan masukan dan saran untuk pengembangan program lebih lanjut. Terima kasih!
