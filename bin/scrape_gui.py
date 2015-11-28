# https://www.youtube.com/watch?v=-nmzq3xiZ6I
# http://www.tutorialspoint.com/python/tk_entry.htm


# http://imgur.com/a/r1cG3 "//meta[@property=\"og:image\"]/@content" -d ./temp/

import Tkinter, Tkconstants, tkFileDialog


from web_scraper import scrap_files_from_webpage

class TkFileDialogExample(Tkinter.Frame):
    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        row = 0


        self._source_url_label = Tkinter.Label(self, text="Source URL:").grid(row=row, column=0, sticky=Tkinter.E)

        self._source_url = Tkinter.StringVar(self)

        self._source_url_text = Tkinter.Entry(self, bd=2, textvariable=self._source_url)
        self._source_url_text.grid(row=row, column=1)



        row+=1


        self._destination_directory_label = Tkinter.Label(self, text="Destination:", anchor=Tkinter.E).grid(row=row, column=0, sticky=Tkinter.E)

        self._destination_directory = Tkinter.StringVar(self)

        self._destination_directory_text = Tkinter.Entry(self, bd=2, textvariable=self._destination_directory)
        self._destination_directory_text.grid(row=row, column=1)

        self._select_destination = Tkinter.Button(self, text='Select', command=self._on_click_directory_selector)
        self._select_destination.grid(row=row, column=2)


        row += 1


        self._xpath_selector_label = Tkinter.Label(self, text="XPATH Selector:").grid(row=row, column=0, sticky=Tkinter.E)

        xpath_patterns = [
            "//meta[@property=\"og:image\"]/@content"
        ]

        self._selected_xpath_pattern = Tkinter.StringVar(self)

        self._xpath_pattern_selector = Tkinter.Entry(self, bd=2, textvariable=self._selected_xpath_pattern)
        self._xpath_pattern_selector.grid(row=row, column=1)

        self._common_patterns_selector = Tkinter.OptionMenu(self, self._selected_xpath_pattern, *xpath_patterns,
                                                            command=self._on_common_patterns_change)
        self._common_patterns_selector.grid(row=row, column=2)

        #button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        row += 1

        self._scrape_button = Tkinter.Button(self, text='Scrape!', command=self._on_click_scrape)
        self._scrape_button.grid(row=row, columnspan=3)




        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        # options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        # options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'


    def _on_click_directory_selector(self):

        """Returns a selected directoryname."""

        destination_directory = tkFileDialog.askdirectory(**self.dir_opt)

        self._destination_directory.set(destination_directory)


    def _on_common_patterns_change(self, val):
        print val
        self._selected_xpath_pattern.set(val)

    def _on_click_scrape(self):

        scrap_files_from_webpage(self._destination_directory.get(), self._source_url.get(), self._selected_xpath_pattern.get())




def on_closing():
    root.destroy()


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    root.wm_title("Scraper")
    TkFileDialogExample(root).pack()

    root.mainloop()
