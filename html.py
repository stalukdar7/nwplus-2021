# write-from-py.py

f = open('output.html','wb')

message = """<html>
<head></head>
<body>
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Location</th>
    <th>Coordinates</th>
  </tr>
  <tr>
  </tr>
  <tr>
  </tr>
</table>
</body>
</html>"""

f.write(message)
f.close()
