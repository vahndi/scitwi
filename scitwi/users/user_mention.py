class UserMention(object):

    def __init__(self, user_mention: dict):

        self.id_ = user_mention['id']
        self.indices = user_mention['indices']
        self.name = user_mention['name']
        self.screen_name = user_mention['screen_name']