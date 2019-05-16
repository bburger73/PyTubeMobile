useMe = "visual design"
amount = 5

def downloadFromSearch(vidCount,searchTerm):
    import urllib.request
    import ctypes  # An included library with Python install.   
    import os
    from bs4 import BeautifulSoup
    urls = []
    textToSearch = searchTerm
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        urls.append('https://www.youtube.com' + vid['href'])
    i=0
    dirName = searchTerm
    if len(urls) > 0:
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ")
        else:    
            print("Directory " , dirName ,  " already exists")
        x=0
        while x < vidCount:
            try:
                from pytube import YouTube
                yt = YouTube(urls[i])
                print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloading")
                stream = yt.streams.first()
                stream.download(dirName)
                print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloaded")
                x+=1
            except:
                print("Link " + str(i + 1) + " is not a video.")
            i += 1
        print("Done")
    else:
        print("No Videos found")

downloadFromSearch(amount,useMe)
'''
   ToDo:
        A skip command to skip non videos
''' 