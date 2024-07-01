class RawMsgBean:
    def __init__(self, title, body, is_archive, level):
        self.title = title
        self.body = body
        self.is_archive = is_archive
        self.level = level

    def __repr__(self):
        return f"RawMsgBean(title={self.title}, body={self.body}, is_archive={self.is_archive}, level={self.level})"