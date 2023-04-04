import ftplib
import concurrent.futures
from colorama import Fore, Style

# meminta user memasukkan nama file yang berisi daftar FTP server yang ingin diperiksa
file_name = input("Give Me Your List:  ")

# membuka file dan membaca daftar FTP server
with open(file_name) as file:
    ftp_list = ["ftp." + server.strip() for server in file.readlines()]

# membuka file untuk menyimpan hasil
output_file = open("ftpanon.txt", "w")

# fungsi untuk memeriksa apakah anonymous FTP access diaktifkan
def check_anonymous_ftp(ftp_server):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ftp_server, port=21, timeout=5) # menambahkan timeout 5 detik
        ftp.login()
        ftp.quit()
        return ftp_server
    except ftplib.all_errors:
        return None

# memeriksa setiap FTP pada daftar dan mencetak hasilnya
with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
    future_to_ftp = {executor.submit(check_anonymous_ftp, ftp_server): ftp_server for ftp_server in ftp_list}
    for future in concurrent.futures.as_completed(future_to_ftp):
        ftp_server = future_to_ftp[future]
        result = future.result()
        if result is not None:
            print(Fore.GREEN + f"Anonymous FTP OK pada {result}")
            output_file.write(f"{result}\n")
        else:
            print(Fore.RED + f"Anonymous FTP BAD pada {ftp_server}")
        print(Style.RESET_ALL, end="") # reset warna setelah mencetak

# menutup file setelah selesai
output_file.close()
