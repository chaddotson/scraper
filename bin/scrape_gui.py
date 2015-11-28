
from logging import basicConfig, getLogger, Handler, INFO
from threading import Thread
import Tkinter, Tkconstants, tkFileDialog


from web_scraper import scrap_files_from_webpage


logger = getLogger('')


class WidgetLogger(Handler):
    def __init__(self, widget, level=INFO):
        Handler.__init__(self)
        self.setLevel(level)
        self.widget = widget
        self.widget.config(state='disabled')

    def emit(self, record):
        self.widget.config(state='normal')
        # Append message (record) to the widget
        self.widget.insert(Tkinter.END, self.format(record) + '\n')
        self.widget.see(Tkinter.END)  # Scroll to the bottom
        self.widget.config(state='disabled')



class ScraperFrame(Tkinter.Frame):
    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        self._thread = None

        self._initializeUI()
        self._createCustomLogger()

    def __del__(self):
        if self._thread is not None:
            self._thread.terminate()

    def _initializeUI(self):

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

        row += 1

        self._log_area = Tkinter.Text(self, {"height": 10})
        self._log_area.grid(row=row, columnspan=3)

    def _createCustomLogger(self):

        logger.addHandler(WidgetLogger(self._log_area))
        logger.info("starting")



    def _on_click_directory_selector(self):

        # defining options for opening a directory
        options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Select a folder'

        destination_directory = tkFileDialog.askdirectory(**options)
        self._destination_directory.set(destination_directory)

    def _on_common_patterns_change(self, val):
        self._selected_xpath_pattern.set(val)

    def _on_click_scrape(self):

        self._thread = Thread(target=scrap_files_from_webpage, args=(self._destination_directory.get(), self._source_url.get(), self._selected_xpath_pattern.get()))
        self._thread.start()


        #scrap_files_from_webpage(self._destination_directory.get(), self._source_url.get(), self._selected_xpath_pattern.get())


def main():
    basicConfig(level=INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(levelno)s - %(message)s')

    root = Tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    root.wm_title("Scraper")
    ScraperFrame(root).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
