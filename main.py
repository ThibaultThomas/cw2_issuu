import pandas as pd
import json
import re


from continent import countryToContient
from plot import plot


def readFile(path):
    array = []
    with open(path) as fp:
        line = fp.readline()

        while line:
            j = json.loads(line)
            j["continent"] = countryToContient(j["visitor_country"])
            j["browser"] = j["visitor_useragent"].split("/")[0]
            s = re.sub(r'\(.*?\)', '', j["visitor_useragent"])
            splited = s.split(' ')
            if len(splited) > 5 and len(splited[5].split('/')) > 1:
                j["browser"] = splited[5].split('/')[0]
            array.append(j)
            line = fp.readline()

    return array

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.expand_frame_repr', False)

lines = readFile("issuu_cw2.json")
df = pd.DataFrame.from_dict(lines)
k = df.subject_doc_id.unique()

#for z in k:
    #print(z)
#    if len(plot(df).getViewersOfDocument(z)) > 1:
#        print(z)
#        print(len(plot(df).getViewersOfDocument(z)))

#print(df)

plot(df).topTenDocumentsSeen("140228101942-d4c9bd33cc299cc53d584ca1a4bf15d9", "6a5259b04ccc2fa1")