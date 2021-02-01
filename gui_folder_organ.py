from tkinter import *
from tkinter import filedialog, ttk, messagebox
import os
import shutil

_root = Tk()
_root.title("Folder Organizer")
_root.geometry('400x100')
_root.resizable(width=False, height=False)

_mainframe = ttk.Frame(_root, padding=(5, 5, 5, 5))
_mainframe.grid(row=0, column=0, sticky=(E, W, N, S))

_dir_frame = ttk.Labelframe(_mainframe, text='Directory', padding=(5, 5, 5, 5))
_dir_frame.grid(row=0, column=0, sticky=(E, W))
_dir_frame.columnconfigure(0, weight=1)
_dir_frame.rowconfigure(0, weight=1)


def browse_dir():
    directory = filedialog.askdirectory()
    _dir.set(directory)


_dir = StringVar()
_dir_entry = ttk.Entry(_dir_frame, width=47, textvariable=_dir)
_dir_entry.grid(row=0, column=0, sticky=(E, W, N, S), padx=5)

_browse_btn = ttk.Button(_dir_frame, text='Browse', command=browse_dir)
_browse_btn.grid(row=0, column=1, sticky=(W))

extension_files = {
    'document': ['.doc', '.docx', '.pdf', '.txt', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.wpd'],
    'image': ['.png', '.gif', '.jpg', '.jpeg', '.tiff', '.raw', '.ai', '.bmp', '.ico', '.ps', '.psd', '.svg', '.tif',
              '.tiff'],
    'compressed_file': ['.zip', '.rar', '.z', '.pkg', '.deb', '.7z', '.rpm', '.tar.gz', '.arj'],
    'executable': ['.exe', '.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.gadget', '.jar', '.msi', '.wsf'],
    'video': ['.avi', '.mp4', '.mpeg', '.mkv', '.wmv', '.mov', '.flv', '.webm', '.mpv', '. 3g2', '.3gp', '.h264',
              '.m4v', '.rm'],
    'code': ['.py', '.c', '.swift', '.vb', '.h', '.cs', '.cpp', '.class', '.sh'],
    'internet_related': ['.asp', '.aspx', '.cer', '.cpm', '.js', '.html', '.htm', '.css', '.jsp', '.part', '.php',
                         '.rss', '.xhtml'],
    'audio': ['.wav', '.mp3', '.mpa', '.aif', '.wpl'],
    'database': ['.xml', '.csv', '.db', '.dbf', '.mdb', '.log', '.dat', '.sav', '.sql', '..tar'],
    'fonts': ['.fnt', '.fon', '.otf', '.ttf'],
    'system': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ini', '.sys', '.tmp']
}


def organize():
    directory = _dir.get()
    os.chdir(directory)

    files = os.listdir(directory)
    for file in files:
        name, ext = os.path.splitext(file)
        try:
            for key, value in extension_files.items():
                if ext.lower() in value:
                    filename = key
                    if not os.path.isdir(os.path.join(directory, filename)):
                        os.mkdir(os.path.join(directory, filename))
                        shutil.move(os.path.join(directory, file), os.path.join(directory, filename))
                    else:
                        shutil.move(os.path.join(directory, file), os.path.join(directory, filename))
                    break
        except Exception as e:
            pass
    _alert("Done!")


_organ_btn = ttk.Button(_mainframe, text="Organize", command=organize)
_organ_btn.grid(row=1, column=0, sticky=(E), pady=7, padx=7)


def _alert(msg):
    messagebox.showinfo(message=msg)


_root.mainloop()
