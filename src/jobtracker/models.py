from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class Status(Enum):
    APPLIED = "Applied"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"


@dataclass
class Application:
    company: str
    role: str
    applied_date: date
    status: Status = Status.APPLIED
    location: Optional[str] = None
    job_url: Optional[str] = None
    notes: Optional[str] = None
    id: Optional[int] = None