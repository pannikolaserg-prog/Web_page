from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import urllib.parse


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            file_path = 'page 4.html'

            if not os.path.exists(file_path):
                self.send_response(404)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(f'<h1>404 - Файл {file_path} не найден</h1>'.encode('utf-8'))
                return

            with open(file_path, 'rb') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content)

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(f'<h1>Ошибка: {str(e)}</h1>'.encode('utf-8'))

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')
        params = urllib.parse.parse_qs(data)

        name = params.get('name', [''])[0]
        email = params.get('email', [''])[0]
        message = params.get('message', [''])[0]

        # Вывод в консоль
        print('\n' + '=' * 50)
        print('📩 НОВОЕ СООБЩЕНИЕ')
        print('=' * 50)
        print(f'👤 Имя: {name}')
        print(f'📧 Email: {email}')
        print(f'💬 Сообщение: {message}')
        print('=' * 50)

        # Читаем и возвращаем страницу с уведомлением
        with open('page 4.html', 'r', encoding='utf-8') as f:
            html = f.read()

        alert = f'<div class="alert alert-success alert-dismissible fade show m-3" role="alert">' \
                f'✅ Спасибо, {name}! Ваше сообщение отправлено.' \
                f'<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' \
                f'</div>'
        html = html.replace('<body>', f'<body>{alert}')

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))


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
    print('📝 Данные из формы будут в консоли')
    print('🛑 Для остановки: Ctrl+C')
    print('=' * 50)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n❌ Сервер остановлен')
        httpd.server_close()


if __name__ == '__main__':
    run_server()
