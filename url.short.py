import pyshorteners

def short(url):
    shorten_url = pyshorteners.Shortener()
    print(shorten_url.tinyurl.short(url))

url = input("Enter the url here:\n")
print("\n New url:\n")
short(url)
