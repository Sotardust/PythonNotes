# Define data classes
from dataclasses import dataclass
from typing import List


@dataclass
class PrizeGrade:
    type: int
    typenum: str
    typemoney: str


@dataclass
class LotteryResult:
    name: str
    code: str
    detailsLink: str
    videoLink: str
    date: str
    week: str
    red: str
    blue: str
    blue2: str
    sales: str
    poolmoney: str
    content: str
    addmoney: str
    addmoney2: str
    msg: str
    z2add: str
    m2add: str
    prizegrades: List[PrizeGrade]


@dataclass
class LotteryData:
    state: int
    message: str
    total: int
    pageNum: int
    pageNo: int
    pageSize: int
    Tflag: int
    result: List[LotteryResult]


# Load JSON data
parsed_data = json.loads(data)


# Convert JSON to dataclass instances
def from_dict(data_class, data_dict):
    if isinstance(data_dict, list):
        return [from_dict(data_class, item) for item in data_dict]
    elif isinstance(data_dict, dict):
        fieldtypes = {f.name: f.type for f in data_class.__dataclass_fields__.values()}
        return data_class(**{f: from_dict(fieldtypes[f], data_dict[f]) for f in data_dict})
    else:
        return data_dict


lottery_data = from_dict(LotteryData, parsed_data)
