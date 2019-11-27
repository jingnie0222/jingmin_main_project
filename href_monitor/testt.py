from xml.sax.saxutils import unescape
import requests
import codecs
import re
#from html import unescape
url='http://v.sogou.com.inner/vc/newvr?query=%B1%B1%BE%A9%B5%D8%CC%FA'
req = requests.get(url=url)
#k = re.findall(r'title=\"(.+?)\"', req.text)
#for i in k:
#    print(unescape(i))
#print(req.text.encode('latin-1','ignore').decode('GBK', 'ignore'))
f = req.content.decode('gb18030')
print(f)