from tkinter import *

from data_analyzer import DataAnalyzer
from graph import Graph
from histogram import *


class GUI:

    def callTask2a(self):
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()
        if docTxt is None:
            return
        if fileTxt is None:
            return
            # Show the graph of countries using matplotlib
        p = DataAnalyzer(fileTxt)
        showCountries(p.getCountries(docTxt))
        return

    def callTask2b(self):
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()
        if docTxt is None:
            return
        if fileTxt is None:
            return
            # Show the graph of continents using matplotlib
        p = DataAnalyzer(fileTxt)
        showContinent(p.getContinents(docTxt))
        return

    def callTask3a(self):
        # Show the graph of all the users agents
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()
        if fileTxt is None:
            return
        p = DataAnalyzer(fileTxt)
        showUserAgents(p.getUserAgents())
        return

    def callTask3b(self):
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()
        # Show the graph of views per browser
        if fileTxt is None:
            return
        p = DataAnalyzer(fileTxt)
        showBrowsers(p.getBrowsers())
        return

    def callTask4d(self):
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()

        if docTxt is None:
            return
        if fileTxt is None:
            return
        p = DataAnalyzer(fileTxt)

        # Getting the top 10 files that this user may likes
        # The uuid remove the user from the list
        list = p.topTenDocumentsSeen(docTxt, userTxt)

        # Check if documents has been found
        if list is None or len(list) == 0:
            print("No documents has been found")
        else:
            print("Here the top 10 documents this user may like")
            for i in range(len(list)):
                print("{0}: {1}".format(i + 1, list[i]))
        return

    def callTask5(self):
        userTxt = self.str1.get()
        docTxt = self.str2.get()
        fileTxt = self.str3.get()
        # Creation of a graphviz Graph by calling our object Graph
        if docTxt is None:
            print("Missing document argument")
            exit(1)
        if fileTxt is None:
            print("Missing file argument")
            exit(1)
        p = DataAnalyzer(fileTxt)
        if userTxt is None:
            Graph(p, uuid=None, document=docTxt)
        else:
            Graph(p, uuid=userTxt, document=docTxt)
        return

    def openGui(self):

        ##creating tkinter window
        root = Tk()
        root.geometry('300x100')
        root.title('Coursework 2 - GUI')

        ##generate frames (lines)
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root)
        frame4.pack()

        ##generate buttons
        Button(frame1, text='Task 2a', command=self.callTask2a).pack(side=LEFT)
        Button(frame1, text='Task 2b', command=self.callTask2b).pack(side=LEFT)
        Button(frame1, text='Task 3a', command=self.callTask3a).pack(side=LEFT)
        Button(frame1, text='Task 3b', command=self.callTask3b).pack(side=LEFT)
        Button(frame1, text='Task 4d', command=self.callTask4d).pack(side=LEFT)
        Button(frame1, text='Task 5', command=self.callTask5).pack(side=LEFT)

        ##generate inputbox
        str1 = StringVar()
        str2 = StringVar()
        str3 = StringVar()

        label1 = Label(frame2, text='User Uuid : ').pack(side=LEFT)
        Entry(frame2, textvariable=str1).pack(side=LEFT)

        label2 = Label(frame3, text='Doc Uuid : ').pack(side=LEFT)
        Entry(frame3, textvariable=str2).pack(side=LEFT)

        label3 = Label(frame4, text='File name : ').pack(side=LEFT)
        Entry(frame4, textvariable=str3).pack(side=LEFT)

        ##
        mainloop()
