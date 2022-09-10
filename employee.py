from dataclasses import dataclass
from datetime import date
import uuid

JOB_TITLES = ["SALES_REP", "REGIONAL_MANAGER", "MANAGER", "HR", "ACCOUNTING"]
""":obj:`list` of :obj:`str`: A list of valid job titles at Dunder Mifflin. 
"""


@dataclass
class Employee:
    """Class for keeping track of employee details.

    Args:
        name (str): full name of :obj:`Employee`
        job_title (str): job title

    Attributes:
        employee_id (str): a unique :obj:`Employee` id - generated on construction
    """

    def __init__(self, name: str, job_title: str):
        self.name = name
        self.job_title = job_title
        self.employee_id = uuid.uuid4()

    def update_contact_info(self, name: str) -> str:
        """Update :obj:`Employee`'s contact inforamtion

        Args:
            new_name (str): new :obj:`Employee`'s name

        Returns:
            str: :obj:`Employee`'s old name
        """
        past_name = self.name
        self.name = name
        return past_name

    def promote_employee(self, job_title):
        """Assigns a new job title to :obj:`Employee`

        Args:
            job_title (str): the new job title

        Raises:
            ValueError: If the new job title is not valid
        """

        if job_title not in JOB_TITLES:
            raise ValueError(
                f"Invalid job title {job_title}, expected one of {JOB_TITLES}"
            )
        self.job_title = job_title
