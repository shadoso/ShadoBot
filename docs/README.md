# Import Organization Guidelines:

> ## Imports should be grouped as follows
> - **Alphabetical order** - from **top** to **bottom**.
> 1. **Standard** - library imports.
> 2. **Third-party** - library imports.
> 3. **Local** - module imports.
> 4. **Configuration / Constants** - imports.


> ## Imports should be ordered as follows
> - **Category order** - from **top** to **bottom**.
> - **Alphabetical order** - from **top** to **bottom**.
> - In case of **multiple imports** within a group: **Alphabetical order** - from **left** to **right**.
> 1. **Classes**
> 2. **Functions**
> 3. **Variables**

> ## Exceptions
> - If a module does not need to be imported for the entire code and is only used in a specific part of the code, it
    should be imported within the respective function.

# Example
```python
# Standard
import json
import os

# Third-party
from pathlib import Path

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import __version__

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

# Local
from absolute_path import cog_description, cog_list

from languages.excluded_languages import exclude

# Configuration
from config.config import settings

from config.constants import LAST_ELEMENT_, PERCENTAGE_
```
