# write-from-py.py

f = open('output.html','wb')

message = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>
<table style="width:100%">
  <tr>
    <th>Event Name</th>
    <th>Date Happened</th>
    <th>Type of Disaster</th>
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
