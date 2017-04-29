
def get_message(wishlist, Person_name):

	message = []
	if wishlist:
		for x in wishlist:
			message.append('''<div class="display-wishlist"><div><h1>'''+ str(x.title) +'''</h1></div><div><img src="'''+ str(x.image_url) +'''" style="max-width:100%"></div><div><div class="cta" style="margin: 20px;"><a href="'''+ str(x.item_url) +'''" style="color: white;text-decoration: none;display: inline-block;background: #3D87F5;padding: 10px 20px;border-radius: 5px;">Go to Site</a></div><div><p style="margin: 20px;font-size: 16px;font-weight: 300;color: #666;line-height: 1.5;">'''+ str(x.description) +'''</p></div></div><div class="spacing" style="padding: 20px;background: #4f5b66;"></div></div>''')
		final_message = """\
		<html>
			<head>
				<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
			</head>
			<body>
				<div class="email-background" style="background: #4f5b66;color: #fff;padding: 10px;">
					<div class="logo" style="max-width: 500px;margin: 0 auto;">
						<img src="http://beta.pvaconline.com/wp-content/uploads/2013/10/wishlist.png" alt="" style="max-width: 100%;">
					</div>
					<div class="pre-header" style="background: #4f5b66;color: #fff;padding: 10px;font-family: 'Raleway', sans-serif;font-size: 25px;text-align: center;margin: 20px 0;">
						""" + str(Person_name) + """ has just shared there Wishlist with you. If you wish to perchase one of these items please let """ + str(Person_name)+ """ know.
					</div>
					<div class="email-container" style="max-width: 500px;background: #a7adba;font-family: sans-serif;margin: 0 auto;overflow: hidden;border-radius: 5px;text-align: center;color: #000;">
						"""+ str(''.join(map(str,message))) +"""
					<div class="footer" style="max-width: 500px;background: none;color: #fff;font-family: sans-serif;margin: 0 auto;overflow: hidden;border-radius: 5px;text-align: center;padding: 20px;font-size: 12px;">
						Address | <a href="#" style="color: #3D87F5;">Unsubscibe</a>
					</div>
				</div>
			</body>
		</html>
		"""
		return final_message