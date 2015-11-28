# https://www.youtube.com/watch?v=-nmzq3xiZ6I
# http://www.tutorialspoint.com/python/tk_entry.htm


# http://imgur.com/a/r1cG3 "//meta[@property=\"og:image\"]/@content" -d ./temp/

import Tkinter, Tkconstants, tkFileDialog


class TkFileDialogExample(Tkinter.Frame):
    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        self._destination_directory_label = Tkinter.Label(self, text="Destination:").grid(row=0, column=0)

        self._destination_directory = Tkinter.StringVar(self)

        self._destination_directory_text = Tkinter.Entry(self, bd=2,textvariable=self._destination_directory)
        self._destination_directory_text.grid(row=0, column=1)

        self._select_destination = Tkinter.Button(self, text='Select')
        self._select_destination.grid(row=0, column=2)


        self._xpath_selector_label = Tkinter.Label(self, text="XPATH Selector:").grid(row=1, column=0)

        xpath_patterns = [
            "//meta[@property=\"og:image\"]/@content"
        ]

        self._selected_xpath_pattern = Tkinter.StringVar(self)

        self._xpath_pattern_selector = Tkinter.Entry(self, bd=2,textvariable=self._selected_xpath_pattern)
        self._xpath_pattern_selector.grid(row=1, column=1)

        self._common_patterns_selector = Tkinter.OptionMenu(self, self._selected_xpath_pattern,  *xpath_patterns,
                                                            command=self._onCommonPatternsChange)
        self._common_patterns_selector.grid(row=1, column=2)

        #button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        self._scrape_button = Tkinter.Button(self, text='Scrape!')
        self._scrape_button.grid(row=2, columnspan=3)






        # options for buttons

        # define buttons
        # Tkinter.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)
        # Tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
        # Tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
        # Tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
        # Tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)
        #
        #



        # Tkinter.Label(self, text="XPATH Selector:").pack(side=Tkinter.LEFT)

        # xpath_patterns = [
        #     "//meta[@property=\"og:image\"]/@content"
        # ]
        #
        # self._selected_xpath_pattern = Tkinter.StringVar(self)
        #xpath_patterns_for_option_menu.set(xpath_patterns[0]) # default value

        #common_patterns_selector = apply(Tkinter.OptionMenu, (self, xpath_patterns_for_option_menu) + tuple(xpath_patterns), {command=self.askopenfile})



        # self._xpath_pattern = Tkinter.Entry(self, bd=2,textvariable=self._selected_xpath_pattern).pack(side=Tkinter.LEFT)
        #
        # common_patterns_selector = Tkinter.OptionMenu(self, self._selected_xpath_pattern,  *xpath_patterns,
        #                                               command=self._onCommonPatternsChange)
        # common_patterns_selector.pack()

        # Tkinter.Button(self, text='Scrape it tester').pack(anchor=Tkinter.W)



        #
        #
        # OPTIONS = [
        #     "egg",
        #     "bunny",
        #     "chicken"
        # ]
        #
        # variable = Tkinter.StringVar(root)
        # variable.set(OPTIONS[0]) # default value
        #
        # w = apply(Tkinter.OptionMenu, (self, variable) + tuple(OPTIONS))
        # w.pack()
        #
        #
        # L1 = Tkinter.Label(self, text="User Name")
        # L1.pack(side=Tkinter.LEFT)
        # E1 = Tkinter.Entry(self, bd=5)
        # E1.pack(side=Tkinter.RIGHT)

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


    def _onCommonPatternsChange(self, val):
        print val
        self._selected_xpath_pattern.set(val)


    def askopenfile(self):

        """Returns an opened file in read mode."""

        return tkFileDialog.askopenfile(mode='r', **self.file_opt)

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'w')

    def askdirectory(self):

        """Returns a selected directoryname."""

        return tkFileDialog.askdirectory(**self.dir_opt)


def on_closing():
    root.destroy()


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    TkFileDialogExample(root).pack()

    root.mainloop()
