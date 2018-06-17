
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
            <html><head><title>Calculadora</title></head>
            <body>
            <h1><center>Calculadora</br></br></center></h1>
            <form method="POST"><center>
            First Value:
            <input name="valor1">
            </input>
            Operation:
            <select name ="Op" required>
            <option value="+">Suma</option>
            <option value="-">Resta</option>
            <option value="*">Multiplicacion</option>
            <option value="/">Division</option>
            </select>
            Second Value:
            <input name="valor2">
            </input>
            <input type="submit" name="submit" value="submit">
            </center></form>
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
