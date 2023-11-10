"""app models."""
import pkgutil
from pathlib import Path
from app.db.models.course_activities import CourseActivity  # noqa: F401
from app.db.models.course_student_activity_records import (
    CourseStudentActivityRecord,
)  # noqa: F401
from app.db.models.courses import Course  # noqa: F401
from app.db.models.students import Student  # noqa: F401
from app.db.models.user_courses import UserCourse  # noqa: F401


def load_all_models() -> None:
    """Load all models from this folder."""
    package_dir = Path(__file__).resolve().parent
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="app.db.models.",
    )
    for module in modules:
        __import__(module.name)  # noqa: WPS421
