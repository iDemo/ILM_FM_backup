#!/usr/bin/python3

import urllib.request , re , requests , os

#Websites To Download Media From
URL 	= 'http://www.mstdfr.com/shows/ilm/feed/'
RE 	= 'url="([a-z0-9].*?)"\s'
Podcast	= 'ILM FM'

#Print Our Logo In The Terminal:
print('''\x1b[32m
██╗██╗     ███╗   ███╗    ███████╗███╗   ███╗
██║██║     ████╗ ████║    ██╔════╝████╗ ████║
██║██║     ██╔████╔██║    █████╗  ██╔████╔██║
██║██║     ██║╚██╔╝██║    ██╔══╝  ██║╚██╔╝██║
██║███████╗██║ ╚═╝ ██║    ██║     ██║ ╚═╝ ██║
╚═╝╚══════╝╚═╝     ╚═╝    ╚═╝     ╚═╝     ╚═╝
\x1b[0m''')
print('\x1b[33m' + 'Podcast Episode Backup' + '\x1b[0m')
print('\x1b[35m' + '------------------------------' + '\x1b[0m')
#--------------------------------------------------------------------------
def GetMedia(WebURL , RegularExpression , DirectoryName):
	'''Parses a webpage and get all media URLs that satisfy the resular expression, then downloads them naming them sequencially.'''
	try:
		GoBack = os.getcwd()
		os.mkdir(DirectoryName)
		os.chdir(DirectoryName)
		web = urllib.request.urlopen(WebURL)
		MediaList = list()
		for line in web:
			line = line.decode()
			media = re.findall(RegularExpression,line)
			if media == []:
				continue
			else:
				MediaList.append(media[0])

		for link in enumerate(reversed(MediaList)):
			MediaFile = open('Episode ' + str(link[0]) + '.mp3' , 'wb')
			MediaFile.write(requests.get(link[1]).content)
			MediaFile.close()
			print('\x1b[36m' + '[+]' , '\x1b[34m' + 'Downloaded Episode:' + '\x1b[0m' , link[0])

		os.chdir(GoBack)

	except Exception as TheError:
		print('\x1b[31m' + '[-] ERROR' + '\x1b[0m')
		print(TheError)
#--------------------------------------------------------------------------
GetMedia(URL , RE , Podcast)
