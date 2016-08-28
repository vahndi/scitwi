from scitwi.utils.attrs import str_attr, bool_attr


class UserProfile(object):

    def __init__(self, user: dict):

        self.background_color = str_attr(user, 'profile_background_color')
        self.background_image_url = str_attr(user, 'profile_background_image_url')
        self.background_image_url_https = str_attr(user, 'profile_background_image_url_https')
        self.background_tile = bool_attr(user, 'profile_background_tile')
        self.banner_url = str_attr(user, 'profile_banner_url')
        self.image_url = str_attr(user, 'profile_image_url')
        self.image_url_https = str_attr(user, 'profile_image_url_https')
        self.link_color = str_attr(user, 'profile_link_color')
        self.sidebar_border_color = str_attr(user, 'profile_sidebar_border_color')
        self.sidebar_fill_color = str_attr(user, 'profile_sidebar_fill_color')
        self.text_color = str_attr(user, 'profile_text_color')
        self.use_background_image = bool_attr(user, 'profile_use_background_image')
