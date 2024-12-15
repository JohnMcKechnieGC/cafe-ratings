"""
Define a custom exception that we can use regardless of which database engine we're using.
"""

class DatabaseConnectionError(Exception):
    """Exception raised when a database connection fails."""
