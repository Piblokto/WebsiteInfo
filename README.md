# WebsiteInfo
WebsiteInfo is a simple script I developed for quickly checking information regarding a website, and hosting.
Just simply open the script, and call it with the argument of the website, and the script will do a DNS lookup, and check the information regarding the IP.

So far I have found the script useful for quickly scouting possible vulnerabilities and intelligence about a website, such as if the website is hosted behind a reverse proxy such as CloudFlare. This script could also be simply adapted to reach out to other API's, as well as other security vulnerability tools like nmap to check open and vulnerable ports on the web server.
<img src="https://i.ibb.co/P5QFMbP/websiteinfo-screenshot.png" alt="websiteinfo-screenshot" border="0">


### Installation
Simply clone the GitHub repository. Then install the requirements using `pip install -r requirements.txt`.

For the best experience it's best to add to make the script executable, and add it to your path.

Otherwise you can create an alias in your .bash_profile or .zshrc for 
`alias websiteinfo='python3 location/of/script.py'`

To use the script properly you will require an IPInfo API key which you can get for [free](https://ipinfo.io/). Then paste this key into line 12 of the script.

### Usage
Depending on how you've installed it usage will vary. As I'm not too versed with bash scripts, I'm open to any pull requests with automated setup scripts.
