import redis

from redis_lru import RedisLRU

from models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def search_author(fname):
    authors = Author.objects()
    return authors(fullname__istartswith=fname)


@cache
def search_quote(tag):
    quotes = Quote.objects()
    return quotes(tags__contains=tag)


def output_response(response):
    for record in response:
        print(record.to_json())


def quote():
    while True:
        command = input("Enter query(command:values): ")

        if command.lower() == 'exit':
            break

        command, values = command.split(':')

        if command.lower() == 'name':
            print(f"Author with name '{values}':")
            output_response(search_author(values))

        elif command.lower() == 'tag':
            print(f"Quotes with tag '{values}':")
            output_response(search_quote(values))

        elif command.lower() == 'tags':
            new_values = values.split(',')
            quote_list = []
            for value in new_values:
                if search_quote(value) not in quote_list:
                    quote_list.append(search_quote(value))
            print(f"Quotes with tags '{values}':")
            output_response(quote_list)


if __name__ == '__main__':
    quote()

