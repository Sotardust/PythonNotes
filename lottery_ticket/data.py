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

