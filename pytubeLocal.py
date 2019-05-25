
def getArray(fileName):
    f = open(fileName,"r")
    strng = f.read()
    outArr = strng.split(",")
    return outArr

def addElement(fileName,newElement):
    f = open(fileName,"a")
    f.write(newElement + ",")
    f.close()

def fileContains(fileName,inElement):
    holdArr = getArray(fileName)
    if inElement in holdArr:
        return True
    else:
        return False

def getYoutubeLinks(searchTerm):
    import urllib.request
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
    return urls

def createLocation(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")

def download(url):
    from pytube import YouTube
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(dirName)
    addElement(kirName + "downloadLinks.txt",url)


def downloadLoop(dirName,kirName,urls,):
    createLocation(dirName)
    i=0
    x=0
    while x < vidCount:
        try:
            while fileContains(kirName + "downloadLinks.txt",urls[i]):
                i += 1
            print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloading")
            download(url[i])
            print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloaded")
            x += 1
        except:
            print("Link " + str(i + 1) + " is not a video.")
            i += 1
    print("Done")


def downloadFromSearch(vidCount,searchTerm):
    import ctypes  # An included library with Python install.   
    import os
    urls = getYoutubeLinks(searchTerm)
    i=0
    x=0
    kirName = 'C:\\Users\\Ben\\Desktop\\Youtube\\'
    dirName = kirName + searchTerm
    if len(urls) > 0:
        createLocation(dirName)
        while x < vidCount:
            try:
                while fileContains(kirName + "downloadLinks.txt",urls[i]):
                    i += 1
                print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloading")
                download(url[i])
                print("Video " + str(x + 1) + " out of " + str(vidCount) + " downloaded")
                x += 1
            except:
                print("Link " + str(i + 1) + " is not a video.")
                i += 1
        print("Done")
    else:
        print("No Videos found")
    ctypes.windll.user32.MessageBoxW(0, "Downloading " + searchTerm + " Completed", "Alert",1)
