from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to access datastore ...

class Mynetwork(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      useremail = ''
      usernetwork = ''
      usernetworkrq = ''
      userslist = []
      content = ''
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremail = users.get_current_user().email()
      query = Usersnetworktable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         usernetworkrq = userdetails.usernetworkrq
         usernetwork = userdetails.usernetwork
      usernetworkrq = usernetworkrq.split()
      usernetwork = usernetwork.split()
      query = Userstable.all()
      queryresults = query
      for userdetails in queryresults:
         userslist.append(userdetails.useremail)
      userslist.remove(useremail)
      userslist.sort()
      for user in userslist:
         if user in usernetworkrq:
            query = Userstable.all()
            query.filter('useremail',user)
            queryresults = query.fetch(1,0)
            for userdetails in queryresults:
               imagekey = userdetails.key()
               username = userdetails.username
               content = content + ''' <li data-theme="e"> 
                                                <a href="/viewmynetwork?email=%s"> 
                                                  <img class="ui-li-thumb" src="/getimage?key=%s">
				                  <span class="textaddtonetwork">%s<br><br></span>
                                                  <span class="textaddtonetwork">%s<br>connection request</span>
                                                </a> 
					</li>'''%(user, imagekey, username, user)
      for user in userslist:
         if user in usernetwork:
            query = Userstable.all()
            query.filter('useremail',user)
            queryresults = query.fetch(1,0)
            for userdetails in queryresults:
               imagekey = userdetails.key()
               username = userdetails.username
               content = content + ''' <li> 
                                                <a href="/viewmynetwork?email=%s"> 
                                                  <img class="ui-li-thumb" src="/getimage?key=%s">
				                  <span class="textaddtonetwork">%s<br><br></span>
                                                  <span class="textaddtonetwork">%s</span>
                                                </a> 
					</li>'''%(user, imagekey, username, user)
      if len(usernetworkrq) == 0 and len(usernetwork) == 0:
         content = '<div class="content" data-role="content" data-theme="a" align="center"><br/><br/><b>sorry! you have no network ...</b><br/><br/></div>'
      
      header = '''<!doctype html> 
<html>
	<head>
		<meta name="HandheldFriendly" content="true" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; minimum-scale=1.0; maximum-scale=1.0;" />
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
		<link type="text/css" rel="stylesheet" href="jscss/jqmcss.css" />
		<link type="text/css" rel="stylesheet" href="jscss/style.css" />
		<script type="text/javascript" src="jscss/jqjs.js"></script>
                <script type="text/javascript" src="jscss/custom.js"></script> 
		<script type="text/javascript" src="jscss/jqmjs.js"></script> 
                <title> 
			Rideshare-Ke
		</title> 
	</head> 
	<body>
		<div data-role="page" data-theme="a"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>'''
      content = ''' <div class="content" data-role="content" data-theme="d"> 
			<ul data-role="listview" data-filter="true" data-filter-placeholder="search" data-theme="a">''' + content + '''</ul> </div>'''

      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li>
		<a onclick="url='/ridessharedaroundme';getridessharedaroundme();"> 
			rides shared
		</a> 
	</li>
        <li> 
		<a onclick="url='/liftseekersaroundme';getliftseekersaroundme();"> 
			lift seekers
		</a> 
	</li>
        <li> 
		<a href="/postridelogin"> 
			share ride
		</a> 
	</li>
        <li> 
		<a href="/seekliftlogin"> 
			seek lift
		</a> 
	</li>
        <li> 
		<a href="/aboutlogin"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/helplogin"> 
			help
		</a> 
	</li>
        <li> 
		<a href="/logout"> 
			log out
		</a> 
	</li>
</ul>
<div data-role="navbar" data-theme="a">
	<ul><li><a href="/ridesharekenyalogin">main<br/>menu</a></li>
	<li><a href="/myaccount">my<br/>account</a></li>
	<li><a href="/mynetwork">my<br/>network</a></li>
	<li><a href="/addtonetwork">add to<br/>network</a></li></ul>
</div>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class mynetwork ...
