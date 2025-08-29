import socket

def create_socket_server(host='localhost', port=8080):
    # ایجاد سوکت
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # بایند کردن به host و port
    server_socket.bind((host, port))
    
    # گوش دادن به اتصالات
    server_socket.listen(5)
    print(f"سرور در حال اجرا روی {host}:{port}")
    
    try:
        while True:
            # پذیرش اتصال
            client_socket, client_address = server_socket.accept()
            print(f"اتصال از: {client_address}")
            
            # دریافت داده
            data = client_socket.recv(1024).decode('utf-8')
            print(f"داده دریافتی: {data}")
            
            # پاسخ به کلاینت
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>سلام! سرور پایتون فعال است</h1>"
            client_socket.send(response.encode('utf-8'))
            
            # بستن اتصال
            client_socket.close()
            
    except KeyboardInterrupt:
        print("\nسرور در حال خاموش شدن...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    create_socket_server('0.0.0.0', 8080)  # گوش دادن به همه اینترفیس‌ها
