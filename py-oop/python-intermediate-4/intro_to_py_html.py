import webbrowser,os

file1 = open('data.html', 'w')
file1.write(''' <html> 
                    <head>
                        <title>HTML and Python </title>
                    </head>
                    
                    <body>
                        <h1 align ='center'>Student Data </h1>
                        <table border = '1' align ='center' width = '50%'>
                            <tr>
                                <th>Id</th>
                                <th>Name</th>
                            </tr>
                            <tr>
                                <td>1001</td>
                                <td>Kim</td>
                            </tr>
                            <tr>
                                <td>1002</td>
                                <td>Sam</td>
                            </tr>
                        </table>
                    </body>
                </html>                    
''')
file1.close()
webbrowser.open('file://' + os.path.realpath('data.html')) # universal
# webbrowser.open('data.html') # windows only