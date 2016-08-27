class StatusMetadata(object):

    def __init__(self, metadata: dict):

        self.iso_language_code = metadata['iso_language_code']
        self.result_type = metadata['result_type']