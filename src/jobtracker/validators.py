import datetime
from datetime import date

from jobtracker.exceptions import ValidationError
from jobtracker.models import Status


def validate_required_text(value: str, field_name: str) -> str:
    """Return the text stripped of spaces; raise error if it is empty."""
    cleaned = value.strip()
    if not cleaned:
        raise ValidationError(f"{field_name} cannot be empty.")
    return cleaned


def validate_status(value: str) -> Status:
    """Convert user text like 'interview' into a Status member."""
    try:
        return Status(value.strip().capitalize())
    except ValueError:
        allowed = ", ".join(s.value for s in Status)
        raise ValidationError(f"Status must be one of: {allowed}.")


def parse_date(value: str) -> date:
    """Convert 'YYYY-MM-DD' text into a date object."""
    try:
        if value.strip():
            return date.fromisoformat(value.strip())
        else:
            return date.today()

    except ValueError:
        raise ValidationError("Date must be in YYYY-MM-DD format.")
