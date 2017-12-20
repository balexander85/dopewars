"""These are the exception classes."""


class NoOptionFoundException(Exception):
    """
       The user attempted to select an
       option that is not available.
    """
    pass


class InsufficientFundsException(Exception):
    """
       The user does not have sufficient funds
       for purchase
    """
    pass


class UnableToTravelException(Exception):
    """
       Not implemented yet, players are not able to leave yet
    """
    pass
