"""Generic errors"""
class EntityException(Exception):
    """Entity Exception"""
    def __init__(self, message: str):
        self.message = message
