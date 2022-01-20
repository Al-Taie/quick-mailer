class ImageNotFoundError(FileNotFoundError):
    """Exception raised when image not exists.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Image not exists in a path!"):
        self.message = message
        super().__init__(self.message)


class AudioNotFoundError(FileNotFoundError):
    """Exception raised when audio not exists.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Audio not exists in a path!"):
        self.message = message
        super().__init__(self.message)


class OutboundSpamException(Exception):
    """Exception raised when Account need to verify.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Please Login To Your Account And Verify it."):
        self.message = message
        super().__init__(self.message)
