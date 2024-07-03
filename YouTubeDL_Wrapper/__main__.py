def gui():
    """ Simple Gui for yt-dlp"""
    from tkinter import Tk,Entry,Label,Frame,Button,StringVar,ttk
    from Wrap_ytdl import YouTube_DL
    import threading

    def downloadLink(*args):
        link_t = True if linktype_box.get() == 'Playlist' else False
        youtubeLink = YouTube_DL(url_entry.get(),ops_box.get(),link_t)
        youtubeLink.download_YTLink()

    def clearEntry(*args):
        url_entry.delete(0,'end')
    
    root = Tk()
    root.title('YouTube Download')
    root.geometry('400x160+200+200')
    root.resizable(False,False)

    url_entry = Entry(root)
    url_entry.insert(0,'Enter your Youtube Link ..')
    url_entry.configure(width=100)
    url_entry.pack(side='top',padx=20,pady=15)
    url_entry.bind('<Button-1>',clearEntry)
    
    #LinkTypes
    options_frame = Frame(root,background='black')
    linktype_label = Label(options_frame,text='Link Type',width=20)
    lt = StringVar(root)
    lt_options = ['Playlist','Single']
    lt.set(lt_options[0])
    linktype_box = ttk.Combobox(options_frame,textvariable=lt,values=lt_options)
    linktype_label.pack(side='left')
    linktype_box.pack()
    
    #Options
    options_frame2 = Frame(root,background='black')
    options_label = Label(options_frame2,text='Options',width=20)
    ops = StringVar(root)
    ops_options = ['Audio','Video']
    ops.set(ops_options[0])
    ops_box = ttk.Combobox(options_frame2,textvariable=ops,values=ops_options)
    options_label.pack(side='left')
    ops_box.pack()

    options_frame.pack()
    options_frame2.pack()

    download_button = Button(root,text='Download',width=40,command=lambda: threading.Thread(target=downloadLink).start())
    download_button.pack(pady=20)


    root.mainloop()


if "__main__" == __name__:
    gui()