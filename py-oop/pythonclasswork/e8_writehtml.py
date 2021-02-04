import webbrowser, os

file1 = open("index.html", "w")
file1.write('''
        <html>
            <head>
                    <title> Html from python </title>
            </head>
            <body>
                <h1>Employee Data</h1>
                <table border = '1' width = '50%'>
                    <tr><th>ID</th><th>Name</th></tr>  <!--table header -->
                    <tr><th>1001</th><th>Bob</th></tr> <!--table data -->
                    <tr><th>1002</th><th>Maria</th></tr>
                    </table>
            </body>
        </html>
''')

webbrowser.open("index.html")
#webbrowser.open("file://"+os.path.realpath("index.html"))