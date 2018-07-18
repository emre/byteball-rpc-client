class ByteBallRPCException(Exception):
    # extended the default Exception, we can seperate from the
    # built-in exceptions and store the error code in the JSON-RPC
    # response.
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
