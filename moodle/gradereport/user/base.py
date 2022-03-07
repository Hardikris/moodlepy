from typing import List, Optional
from moodle import BaseMoodle



class BaseUser(BaseMoodle):
    def get_grade_items(self, courseid: int, userid: Optional[int] = 0, groupid: Optional[int] = 0):
        """Returns the complete list of grade items for users in a course

        Args:
            courseid (int): course id
            userid (Optional[int]): user id
            groupid (Optional[int]): group id

        Returns:
            List[Section]: list of section
        """
        data = self.moodle.post(
            "gradereport_user_get_grade_items",
            courseid=courseid,
            userid=userid,
            groupid=groupid
        )
        return data
