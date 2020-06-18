from django.http import Http404


class Post:
    POSTS = [
        {'id': 1, 'title': 'First Post', 'content': 'This is my first post'},
        {'id': 2, 'title': 'Second Post', 'content': 'This is my second post'},
        {'id': 3, 'title': 'Third Post', 'content': 'This is my third post'},
        {'id': 4, 'title': 'Forth Post', 'content': 'This is my forth post'},
        {'id': 5, 'title': 'Fifth Post', 'content': 'This is my fifth post'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404('Sorry post #{} not found.'.format(id))
