class UserProfile(object):

    def __init__(self, user: dict):

        self.background_color = user['profile_background_color']
        self.background_image_url = user['profile_background_image_url']
        self.background_image_url_https = user['profile_background_image_url_https']
        self.background_tile = user['profile_background_tile']
        self.banner_url = user['profile_banner_url']
        self.image_url = user['profile_image_url']
        self.image_url_https = user['profile_image_url_https']
        self.link_color = user['profile_link_color']
        self.sidebar_border_color = user['profile_sidebar_border_color']
        self.sidebar_fill_color = user['profile_sidebar_fill_color']
        self.text_color = user['profile_text_color']
        self.use_background_image = user['profile_use_background_image']
