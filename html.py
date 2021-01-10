# write-from-py.py

f = open('output.html','wb')

message = """<html>
<head></head>
<body><p>Output</p></body>
</html>"""

f.write(message)
f.close()
