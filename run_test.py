import pytest

if __name__ == "__main__":
    pytest.main(["-s", "-m", "regression", "--alluredir=./reports"])
