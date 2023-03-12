import json

from models import Author, Quote


def open_file(file_name):
    with open(file_name, "r", encoding="utf-8") as fn:
        data = json.load(fn)
    return data


def insert_authors(file_name):
    # Author.drop_collection()
    dict_authors = open_file(file_name)
    for author in dict_authors:
        new_author = Author(fullname=author['fullname'])
        new_author.born_date = author['born_date']
        new_author.born_location = author['born_location']
        new_author.description = author['description']
        new_author.save()


def insert_quotes(file_name):
    # Quote.drop_collection()
    authors = Author.objects()
    for author in authors:
        print(author.to_mongo().to_dict()['_id'])
    dict_quotes = open_file(file_name)
    for quote in dict_quotes:
        new_quote = Quote(tags=quote['tags'])
        new_quote.author = Author.objects(fullname = quote['author'])[0].to_mongo().to_dict()['_id']
        print(new_quote.author)
        new_quote.quote = quote['quote']
        new_quote.save()


if __name__ == '__main__':
    insert_authors('authors.json')
    insert_quotes('quotes.json')
