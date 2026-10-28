import datetime
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
        else:
            raise NotVaccinatedError("NotVaccinatedError")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
