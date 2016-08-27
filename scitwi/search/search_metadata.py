class SearchMetadata(object):

    def __init__(self, metadata: dict):

        self.completed_in = metadata['completed_in']
        self.count = metadata['count']
        self.max_id = metadata['max_id']
        self.query = metadata['query']
        self.refresh_url = metadata['refresh_url']
        self.since_id = metadata['since_id']

