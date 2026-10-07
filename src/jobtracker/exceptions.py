class JobTrackerError(Exception):
    """Base class for all errors raised by this application."""


class ValidationError(JobTrackerError):
    """User input is missing or invalid."""


class RecordNotFoundError(JobTrackerError):
    """No application exists with the requested ID."""


class DatabaseError(JobTrackerError):
    """Something went wrong while reading from or writing to the database."""

