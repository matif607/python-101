class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function


@is_authenticated_decorator('/<user>')
def create_blog_post(user):
    print(f"this is {user.name}'s blog post")


new_user = User("atif")
new_user.is_logged_in = True
create_blog_post(new_user)