import json
import re

import pandas as pd

from continent import countryToContient


class DataAnalyzer:

    def __init__(self, path: str) -> None:
        """
        Create a DataAnalyzer object

        :param path: The path
        """
        lines = self.readFile(path)
        self.dataframe = pd.DataFrame.from_dict(lines)

    def getCountries(self, docid: str) -> list:
        """

        :param docid: The document uuid
        :return: A list containing the countries associated
        """
        countries = self.dataframe[self.dataframe.subject_doc_id == docid]
        data = countries["visitor_country"].dropna()
        return data

    def getContinents(self, docid: str) -> list:
        """

        :param docid: The document uuid
        :return: A list containing the continents associated
        """
        countries = self.dataframe[self.dataframe.subject_doc_id == docid]
        data = countries["continent"].dropna()
        return data

    def getBrowsers(self) -> list:
        """

        :return: A list containing all browser parsed inside the user agents
        """
        data = self.dataframe["browser"].dropna()
        return data

    def getUserAgents(self) -> list:
        """

        :return: The list of all user agent with no formatting
        """
        data = self.dataframe["visitor_useragent"].dropna()
        return data

    def getViewersOfDocument(self, docid: str) -> list:
        """

        :param docid: The document id
        :return: All the viewers who saw this document
        """
        docs = self.dataframe[self.dataframe.subject_doc_id == docid]
        ids = docs["visitor_uuid"].dropna().unique()
        return list(ids)

    def getDocumentsSeen(self, visitor_uuid: str) -> list:
        """

        :param visitor_uuid: The visitor uuid
        :return: All the document that saw this client
        """
        ids = self.dataframe[self.dataframe.visitor_uuid == visitor_uuid]
        docs = ids["subject_doc_id"].dropna().unique()
        return list(docs)

    def alsoLikedDocuments(self, docid: str, visitorid: str) -> list:
        """

        :param docid: The document uuid
        :param visitorid: The visitor uuid (optional)
        :return: A list of 'similar' files
        """
        docs = self.getViewersOfDocument(docid)
        array = []
        for z in docs:
            if visitorid is None or visitorid != z:
                for k in self.getDocumentsSeen(z):
                    if k != docid:
                        array.append(k)
        return array

    def userHasReadDocument(self, doc_uuid: str, client_uuid: str) -> bool:
        """

        :param doc_uuid: The document uuid
        :param client_uuid: The uuid of the client
        :return: A boolean
        """
        if client_uuid is None:
            return False
        viewers = self.getViewersOfDocument(doc_uuid)
        return client_uuid in viewers

    def topTenDocumentsSeen(self, docid: str, visitorid: str) -> list:
        """

        :param docid: The document uuid
        :param visitorid: The visitor uuid
        :return: A list of the 10 most similar documents
        """
        array = self.alsoLikedDocuments(docid, visitorid)
        new_list = sorted(array, key=array.count, reverse=True)
        new_set = set(new_list)
        if len(new_set) > 10:
            return list(new_set)[:10]
        return list(new_set)

    def topTenDocumentsWithAuthor(self, docid: str, visitorid: str) -> dict:
        """

        :param docid: The document uuid
        :param visitorid: The visitor uuid (optional)
        :return: A dictionary of <Document> <List of reader> of at maximum 10 keys
        """
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

    def readFile(self, path) -> list:
        """

        :rtype: list
        :param path: The path of the file
        :return: A list of each line of the file
        """
        array = []
        with open(path) as fp:
            line = fp.readline()

            # While line is valid do
            while line:
                j = json.loads(line)
                j["continent"] = countryToContient(j["visitor_country"])

                # Here, a regex has been used to get the browser
                j["browser"] = j["visitor_useragent"].split("/")[0]
                s = re.sub(r'\(.*?\)', '', j["visitor_useragent"])
                splited = s.split(' ')
                if len(splited) > 5 and len(splited[5].split('/')) > 1:
                    j["browser"] = splited[5].split('/')[0]
                # Add the line to the array
                array.append(j)
                line = fp.readline()

        return array
