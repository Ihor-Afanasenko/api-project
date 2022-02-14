from __future__ import annotations

import uuid
from datetime import datetime
from typing import List
from _pytest.reports import TestReport


class Result:
    def __init__(
            self,
            id: str,
            name: str,
            result: str,
            date_created: datetime,
            type: str,
            duration: float,
            log: str,
            std_error: str,
            std_out: str,
    ):
        self.id = id
        self.name = name
        self.result = result
        self.date_created = date_created
        self.type = type
        self.duration = duration
        self.log = log
        self.std_error = std_error
        self.std_out = std_out

    @classmethod
    def from_test_reports(cls, results: List[TestReport], test_type: str) -> List[Result]:
        test_reports = []
        for result in results:
            test_reports.append(cls.from_test_report(result, test_type))

        return test_reports

    @classmethod
    def from_test_report(cls, result: TestReport, test_type: str) -> Result:
        return cls(
            id=str(uuid.uuid4()),
            name=result.head_line,
            result=result.outcome,
            date_created=datetime.now(),
            type=test_type,
            duration=result.duration,
            log=result.caplog,
            std_error=result.capstderr,
            std_out=result.capstdout
        )

    def to_dict(self):
        data = dict()

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = str(value)
            data[key] = value

        return data
