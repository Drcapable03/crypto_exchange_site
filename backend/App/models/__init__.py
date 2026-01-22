 # backend/app/models/__init__.py
from .base import Base
from .user import User
from .balance import Balance
# Add future models here

# ... (keep existing top imports: logging, sys, os, etc.)

# Explicitly import models to force table registration on Base.metadata
# This is the key: import here, in env.py's global scope
# from app.models.base import Base
# from app.models.user import User
# from app.models.balance import Balance

# If you have __init__.py in models/ with imports, you can do:
# from app.models import Base, User, Balance

target_metadata = Base.metadata

# Debug print to confirm during alembic runs (add this temporarily)
# print("DEBUG: Tables registered in target_metadata:")
# for t in target_metadata.tables:
#     print("  -", t)