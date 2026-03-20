from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Путь к вашему HTML файлу в корне
            file_path = 'page 4.html'  # или любое другое имя

            # Проверяем, существует ли файл
            if not os.path.exists(file_path):
                self.send_response(404)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(f'<h1>404 - Файл {file_path} не найден</h1>'.encode('utf-8'))
                return

            # Читаем HTML файл
            with open(file_path, 'rb') as file:
                content = file.read()

            # Отправляем заголовки
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Отправляем содержимое
            self.wfile.write(content)

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(f'<h1>Ошибка: {str(e)}</h1>'.encode('utf-8'))


def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('=' * 50)
    print('🚀 СЕРВЕР ЗАПУЩЕН')
    print('=' * 50)
    print(f'📁 Текущая папка: {os.getcwd()}')
    print(f'📄 Файлы HTML: {[f for f in os.listdir(".") if f.endswith(".html")]}')
    print('=' * 50)
    print('🌐 Откройте в браузере: http://localhost:8080')
    print('🛑 Для остановки: Ctrl+C')
    print('=' * 50)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n❌ Сервер остановлен')
        httpd.server_close()


if __name__ == '__main__':
    run_server()