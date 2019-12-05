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
        plt.figure()
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
        c = countries["visitor_country"]
        self.showPlot(c, "Country", "Occurrences", "Number of occurrences per country")


    def showContinent(self, docid):
        countries = self.dataframe[self.dataframe.subject_doc_id == docid]
        c = countries["continent"]
        self.showPlot(c, "Continent", "Occurrences", "Number of occurrences per Continent")

    def viewPerBrowser(self):
        c = self.dataframe["browser"]

        self.showPlot(c, "Browser", "Occurrences", "Number of occurrences per browser")

    def viewPerUserAgent(self):
        z = self.dataframe["visitor_useragent"]

        self.showPlot(z, "User-agent", "Occurrences", "Number of useragent")

    def getViewersOfDocument(self, docid):
        docs = self.dataframe[self.dataframe.subject_doc_id == docid]
        ids = docs["visitor_uuid"].dropna().unique()
        return list(ids)

    def getDocumentsSeen(self, visitor_uuid):
        ids = self.dataframe[self.dataframe.visitor_uuid == visitor_uuid]
        docs = ids["subject_doc_id"].dropna().unique()
        return list(docs)

    def alsoLikedDocuments(self, docid, visitorid):
        docs = self.getViewersOfDocument(docid)
        print(docs)
        array = []
        for z in docs:
            if visitorid is None or visitorid != z:
                for k in self.getDocumentsSeen(z):
                    if k != docid:
                        array.append(k)
        return array

    def userHasReadDocument(self, docid, uuid):
        if uuid is None:
            return False
        viewers = self.getViewersOfDocument(docid)
        return uuid in viewers

    def topTenDocumentsSeen(self, docid, visitorid):
        array = self.alsoLikedDocuments(docid, visitorid)
        new_list = sorted(array, key=array.count, reverse=True)
        new_set = set(new_list)
        if len(new_set) > 10:
            return list(new_set)[:10]
        return list(new_set)

    def topTenDocumentsWithAuthor(self, docid, visitorid):
        array = self.topTenDocumentsSeen(docid, visitorid)
        viewer = self.getViewersOfDocument(docid)
        mp = {}
        for doc in array:
            viewers = self.getViewersOfDocument(doc)
            for u in set(viewers):
                if u in viewer:
                    if doc in mp:
                        mp[doc].append(u)
                    else:
                        mp[doc] = []
                        mp[doc].append(u)
        return mp
