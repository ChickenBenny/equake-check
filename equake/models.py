from pydantic import BaseModel
import datetime

class EquakeData(BaseModel):
    datatime_in_tw: datetime.datetime
    scale: float
    depth: float
    location: str
