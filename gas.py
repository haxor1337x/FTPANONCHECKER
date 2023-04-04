import ftplib
import concurrent.futures

file_name = input("Give Me Your List:  ")

with open(file_name) as file:
    ftp_list = ["ftp." + server.strip() for server in file.readlines()]

output_file = open("ftpanon.txt", "w")

def check_anonymous_ftp(ftp_server):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ftp_server, port=21, timeout=5) # menambahkan timeout 5 detik
        ftp.login()
        ftp.quit()
        return ftp_server
    except ftplib.all_errors:
        return None

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_to_ftp = {executor.submit(check_anonymous_ftp, ftp_server): ftp_server for ftp_server in ftp_list}
    for future in concurrent.futures.as_completed(future_to_ftp):
        ftp_server = future_to_ftp[future]
        result = future.result()
        if result is not None:
            print(f"Anonymous FTP OK pada {result}")
            output_file.write(f"{result}\n")
        else:
            print(f"Anonymous FTP BAD pada {ftp_server}")

output_file.close()
