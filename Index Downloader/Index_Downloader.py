from tkinter import *
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests
from clint.textui import progress

main_window = Tk()
dir = StringVar()
links = []
CHUNK_SIZE = 256


def get_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in (soup.find_all('a')):
        links.append(link['href'])


def download(url_list):
    for link in url_list:
        req = requests.get(url + '/' + link, stream = True)
        try:
            with open(path + link, "wb") as file:
                length = int(req.headers.get('content-length'))
                for chunk in progress.bar(req.iter_content(CHUNK_SIZE), expected_size = (length/CHUNK_SIZE), label = link + "  "):
                    if chunk:
                        file.write(chunk)
                print("Download Successful\n")
            
        except OSError as e:
            continue


def browse_directory():
    path = filedialog.askdirectory()
    dir.set(path)

def main():
    print("Enter 'Index Of' URL")
    url = input()
    print("Enter The Path To Save Files")
    #path = input()
    
    print("")


def test():
    main_window.title("Index Downloader")
    main_window.geometry('420x80')
    menu = Menu(main_window)
    main_window.config(menu = menu)
    file_menu = Menu(menu)
    menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "Exit", command = main_window.quit)

    Label(main_window, text = "Index Of URL").place(x = 5, y = 0)
    Entry(main_window, width = 40).place(x = 100, y = 0)
    Label(main_window, text = "Save Directory").place(x = 5, y = 30)
    Entry(main_window, width = 40, textvariable = dir).place(x = 100, y = 30)
    Button(main_window, text = "Browse", command = browse_directory).place(x = 360, y = 25)

    main_window.mainloop()

test()

