import json
def get_articles():
    with open('articles.json', 'r', encoding='utf-8') as fox:
        foxy = json.load(fox)
        return foxy
def save_article(name, text):
    with open("articles.json", 'r', encoding='utf-8') as fox:
        foxy = json.load(fox)
    with open("articles.json", 'w', encoding='utf-8') as fix:
        foxy[name] = text
        json.dump(foxy, fix, ensure_ascii=False)

def delete_article(name):
    with open("articles.json", 'r', encoding='utf-8') as fox:
        foxy = json.load(fox)
    with open("articles.json", 'w', encoding='utf-8') as fix:
        foxy.pop(name)
        json.dump(foxy, fix, ensure_ascii=False)