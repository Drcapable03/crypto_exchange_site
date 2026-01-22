import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from app.models.base import Base
from app.models.user import User
from app.models.balance import Balance

print("Imported successfully")
print("Tables:", list(Base.metadata.tables.keys()))