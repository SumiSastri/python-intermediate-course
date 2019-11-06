import webbrowser, os

#exercise 4
file1 = open("index.html" ,"w")
file1.write('''<h1>Hello, This is how python is embedded in an html file</h1>''')
file1.close()
webbrowser.open("file://" + os.path.realpath("index.html"))

#exercise 5

file1 = open("index2.html", "w")
file1.write('''<html>
                    <head>
                        <title>Html from python</title>
                    </head>
                    <body>
                        <h1 align='center'>Employee Salary</h1>
                        <table border='1' width= '50%' align='center'>
                            <tr><th>Employee</th><th>Salary</th></tr>
                            <tr><td>Tom</td><td>25000</td></tr>
                            <tr><td>Michael</td><td>35000</td></tr>
                            <tr><td>Lisa</td><td>15000</td></tr>
                        </table>
                    </body>
               </html>
''')
file1.close()

webbrowser.open("file://"+os.path.realpath("index2.html"))