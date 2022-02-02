#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
print("Content-Type: text/html") 
print()

import cgi
form = cgi.FieldStorage()
pageId = 'Welcome'
print('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Bitnami: Open Source. Simplified</title>
<link href="bitnami.css" media="all" rel="Stylesheet" type="text/css" />
</head>
<body>
<h1><a href="index.py?id=WEB">WEB</a><h1>
<ol>
<li> <a href="index.py?id=HTML">HTML</a></li>
<li> <a href="index.py?id=CSS">CSS</a></li>
<li> <a href="index.py?id=JavaScript">JavaScript</a></li>
</ol>
<h2>{title}</h2>
<div id="container">
  <div id="header"> 
    <div id="bitnami">
        <a href="/"><img alt="Bitnami" src="img/bitnami.png?1186088387" /></a>
    </div>
  </div>
    <div id="menu_launch_page">
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td><img src="img/tab1_welcome.png" alt="" /></td>
        </tr>
      </table>
    </div>
  <div id="lowerContainer">
    <div id="content">
        <div align="center">
<table class="tableParagraph">
<tr>
<td class="container">
<img align="left" src="img/mampstack.png" alt="MAMP packaged by Bitnami"/>
<p>
이제 여기서 부터 파이썬으로 웹서버를 구축하는 것을 해볼테야...  
We created the Bitnami Project to help spread the adoption of freely
available, high quality Open Source web applications. Bitnami aims to make
it easier than ever to discover, download and install Open Source software such 
as document and content management systems, wikis and blogging software.<br/><br/>

You can learn more about Bitnami at <a href="https://bitnami.com">https://bitnami.com</a><br/><br/>

The MAMP packaged by Bitnami is an easy to install
software platform that greatly simplifies the deployment of Open Source web
stacks. It includes ready-to-run versions of
Apache, MariaDB and PHP. MAMP packaged by Bitnami is
distributed for free under the Apache 2.0 license.<br/><br/> 
To get started with MAMP packaged by Bitnami we suggest the following:<br/><br/>


<b>1.- <a target="_blank" href="https://docs.bitnami.com/installer/infrastructure/mamp/">Check our documentation</a></b>. The stack is self-contained and independent on your system, you can find all components in your installation directory: /Applications/mampstack-8.1.1-0<br/><br/>
<b>2.- <a target="_blank" href="https://docs.bitnami.com/installer/infrastructure/mamp/administration/control-services-linux/">Start the servers.</a></b> Open the graphical "Manager" tool in your installation directory to start &amp; stop the installed servers. You can also use "ctlscript.sh" from the command line prompt. <br/><br/>
<b>3.- <a target="_blank" href="https://docs.bitnami.com/installer/infrastructure/mamp/administration/create-custom-application-php/">Deploy your own project</a></b>.
</p>
</td>
</tr>
</table>
        </div>
        <br/><br/>
   </div>
  </div>
</div>
</body>
</html>
'''.format(title=pageId))