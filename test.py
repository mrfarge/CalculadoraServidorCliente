
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:58:38 2018

@author: Maria
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


port = 8181


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("""
            <html><head></head>
            <body>
            <form method="POST">
            First Value:
            <input name="valor1">
            </input>
            Operation:
            <input name="Op">
            </input>
            Second Value:
            <input name="valor2">
            </input>
            <input type="submit" name="submit" value="submit">
            </form>
            </body>
            </html>
            """.encode())

        return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        valor1 = form.getvalue("valor1")
        valor2 = form.getvalue("valor2")
        Op = form.getvalue("Op")
        result = str(eval(valor1 + Op + valor2))
        print(eval(valor1 + Op + valor2))


        self.send_response(200)
        self.end_headers()
        self.wfile.write("<html><head></head>".encode())
        textresult = ("<body><p>El resultado es %s</p>" %result)

        self.wfile.write(textresult.encode())    
        self.wfile.write("</body> </html>".encode())  
            
        return


if __name__ == '__main__':
	server = HTTPServer(('', port), myHandler)        
	try:
		server.serve_forever()

	except KeyboardInterrupt:
		pass
	server.server_close()
