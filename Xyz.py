import os
while True: 
 html = (input ("'\033[94m'what do you want learning: " ))
 os.system('clear')
 if html == "html" :
  print (''' '\033[93m'<!DOCTYPE html>
  <html>
				<head>
								<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
								<meta name="description" content="i love my website">
								<meta charset=""
								<title></title>
				</head>
				<body>
				</body>
</html>
''')
 elif html == "table" :
  print ('''<table border="1">
												<thead>
																<tr>
																				<td>
																								
																				</td>
																</tr>
												</thead>
												<tbody>
																<tr>
																				<td>
																								
																				</td>
																</tr>
												</tbody>
												<tfoot>
																<tr>
																				<td>
																								
																				</td>
																</tr>
												</tfoot>
								</table> ''' )
 elif html == "img" :
  print (" <img src="" alt="" > " )

 elif html == "photo" :
   print (" <img src="" alt="" > " )
 
 elif html == "video" :
     print ('''<video controls>
												<source src="" type="">
								</video> ''')

 elif html == "adio" :
     print (''' <audio controls>
												<source src="" type="">
								</audio> ''' )

 elif html == "input" :
     print (''' <input type="text"placeholder="" > ''')

 elif html == "font size" :
     print (''' <h1></h1>
								<h2></h2>
								<h3></h3>
								<h4></h4>
								<h5></h5>
								<h6></h6> ''')

 elif html == "link" :
     print (''' 	<a href=""></a> ''')
     
 elif html == "head" :
     print (''' <head>
								<meta charset="">
								<link rel="stylesheet" href=".css"></link>
								
								<title></title>
				</head> ''')
				
 elif html == "style" :
     print (''' 	<link rel="stylesheet" href=".css"></link>
								''')
								
 elif html == "JavaScript" :
     print (''' <script></script> ''')
    	
 elif html == "input search":
     print (''' <input type="serch"placeholder="" > ''')
      	
 else:
     print ( "'\033[91m' wrong please try again " )

