def read_data():
    docs = {} 

    n = int(input().strip())

    for _ in range(n):
        tokens = input().strip().split()

        doc_name = tokens[0]
        doc_keywords = tokens[1:]

        for kword in doc_keywords:
            if kword in docs.keys():
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}

    return docs

def search(docs, condition, search_keywords):

    for q in search_keywords:
        if q not in docs.keys():
            search_keywords.remove(q)

    if 0 == len(search_keywords):
        return set()

    found = docs[search_keywords[0]]

    if 'and' == condition:
        for i in range(1, len(search_keywords)):
            if search_keywords[i] in docs.keys():
                found = found.intersection(docs[search_keywords[i]])

    elif 'or' == condition:
        for i in range(1, len(search_keywords)):
            if search_keywords[i] in docs.keys():
                found = found | (found ^ docs[search_keywords[i]])

    else:
        found = set()

    return found

docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )
