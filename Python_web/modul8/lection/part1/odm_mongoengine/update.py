from models import Post, LinkPost, ImagePost, TextPost, User

if __name__ == '__main__':
    # через id не шукається, через pk дивись в read
    # post = Post.objects(id='640d9ba79125aaa2d8ab6e8a')
    # print(post[0].to_mongo.to)
    post = Post.objects(title='MongoEngine Documentation')
    print(post[0].to_mongo().to_dict())
    # post.update(link_url='https://docs.mongoengine.org/apireference.html')
    # print(post[0].to_mongo().to_dict())