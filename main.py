import pandas as pd
import json
import re
import argparse
import os

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

#lines = readFile("sample_100k_lines.json")
#df = pd.DataFrame.from_dict(lines)
#k = df.subject_doc_id.unique()


# for z in k:
# print(z)
#    if len(plot(df).getViewersOfDocument(z)) > 1:
#        print(z)
#        print(len(plot(df).getViewersOfDocument(z)))

# print(plot(df).topTenDocumentsSeen("140228101942-d4c9bd33cc299cc53d584ca1a4bf15d9", "2f63e0cca690da91"))


def main():

    parser = argparse.ArgumentParser(description="Issuu CW2")
    parser.add_argument("-f", "--file", help="JSON file with data", required=True)
    parser.add_argument("-u", "--uuid", help="User uuid")
    parser.add_argument("-d", "--document", help="The document id")
    parser.add_argument("-t", "--task", help="The task of the coursework", required=True)
    args = parser.parse_args()

    task = args.task
    lines = readFile(args.file)
    df = pd.DataFrame.from_dict(lines)
    p = plot(df)

    if task == "2a":
        if args.uuid is None:
            print("Missing uuid argument")
            exit(1)

        p.showCountries(args.uuid)
    elif task == "2b":
        if args.uuid is None:
            print("Missing uuid argument")
            exit(1)
        p.showContinent(args.uuid)

    elif task == "3a":
        p.showCountries(args.uuid)
    elif task == "3b":
        p.showCountries(args.uuid)
    else:
        print("Error: Task not in range [2a, 2b, 3a, 3b, 4d, 5, 6]")


main()
