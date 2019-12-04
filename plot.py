import matplotlib.pyplot as plt
import pandas as pd

class plot:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def showPlot(self, list, xLabel, yLabel, title):
        values = {}
        for k in list:
            if k not in values:
                values[k] = 1
            else:
                values[k] += 1
        plt.style.use('ggplot')

        x = values.keys()
        energy = values.values()

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, energy, color='green')
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)

        plt.xticks(x_pos, x)
        plt.show()

    def showCountries(self, docid):
        countries = self.dataframe[self.dataframe.subject_doc_id == docid]
        #print(countries.head())
        print(self.dataframe)
        c = countries["visitor_country"]
        self.showPlot(c, "Country", "Occurrences", "Number of occurrences per country")


    def showContinent(self, docid):
        countries = self.dataframe[self.dataframe.subject_doc_id == docid]
        #print(countries.head())
        c = countries["continent"]
        self.showPlot(c, "Continent", "Occurrences", "Number of occurrences per Continent")

    def viewPerBrowser(self):
        c = self.dataframe["browser"]
        z = self.dataframe["visitor_useragent"]

        self.showPlot(c, "Browser", "Occurrences", "Number of occurrences per browser")

    def getViewersOfDocument(self, docid):
        docs = self.dataframe[self.dataframe.subject_doc_id == docid]
        ids = docs["visitor_uuid"].dropna().unique()
        return list(ids)

    def getDocumentsSeen(self, visitor_uuid):
        ids = self.dataframe[self.dataframe.visitor_uuid == visitor_uuid]
        docs = ids["subject_doc_id"]
        return list(docs)

    def alsoLikedDocuments(self, docid, visitorid):
        docs = self.getViewersOfDocument(docid)
        array = []
        for z in docs:
            print(z)
            if visitorid is None or visitorid != z:
                for k in self.getDocumentsSeen(z):
                    if k != docid:
                        array.append(k)


        return array

    def topTenDocumentsSeen(self, docid, visitorid):
        array = self.alsoLikedDocuments(docid, visitorid)
        map = {}
        for c in array:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1

        print(map)
