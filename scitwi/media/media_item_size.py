class MediaItemSize(object):

    def __init__(self, size: dict):

        self.height = size['h']
        self.width = size['w']
        self.resize = size['resize']
