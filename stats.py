def get_num_words(result):
    n = result.split()
    count = len(n)
    print(f"Found {count} total words")


def sort_on(items):
    return items["num"]

def get_count_characters(result):
    result = result.lower()
    d = {}
    for i in range(0,len(result)):
        if result[i] != ' ' and result[i] in d:
           d[result[i]] += 1
        else:
           d[result[i]] = 1
    del d[' ']
    l = []
    for i in d:
        d1 = {}
        d1["char"] = i
        d1["num"] = d[i]
        l.append(d1)
    l.sort(reverse=True, key=sort_on)
    for i in l:
        if i["char"].isalpha():
           print(f"{i["char"]}: {i["num"]}")

