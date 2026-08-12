# Run the App

**Without Project Script**

`uv run uvicorn python_code.app:app --reload`


**With Project script add in pyproject.toml**

``` 
[project.scripts]
python-code = "python_code.app:main"

```
**Run this command**

`uv run python-code`