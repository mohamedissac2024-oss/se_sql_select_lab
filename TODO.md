# SQL SELECT Lab Completion TODO

## Approved Plan Steps:

1. ✅ Create TODO.md (current)
2. ✅ Edit main.py Step 1A: Add imports sqlite3 and pandas as pd
3. ✅ Edit main.py Step 1B: conn = sqlite3.connect('data.sqlite')
4. ✅ Edit main.py Step 2: df_first_five query
5. ✅ Edit main.py Step 3: df_five_reverse query
6. ✅ Edit main.py Step 4: df_alias query
7. ✅ Edit main.py Step 5: df_executive CASE query
8. ✅ Edit main.py Step 6: df_name_length LENGTH query
9. ✅ Edit main.py Step 7: df_short_title SUBSTR query
10. ✅ Edit main.py Step 8: sum_total_price SUM query
11. ✅ Edit main.py Step 9: df_day_month_year STRFTIME query
12. ✅ Run `pipenv install` to create the project virtualenv (pandas 2.0.3, pytest 8.3.5)
13. ✅ Run `pytest` to verify all 9 tests pass
14. ✅ Run `python main.py` to print the DataFrames and verify the outputs

## Verification (Linux, Python 3.8.13)

```
$ pipenv install
Virtualenv location: ~/.local/share/virtualenvs/se_sql_select_lab-pX3ChyuT

$ pytest -v
test_main.py::test_connection PASSED
test_main.py::test_step2 PASSED
test_main.py::test_step_3 PASSED
test_main.py::test_step4 PASSED
test_main.py::test_step5 PASSED
test_main.py::test_step6 PASSED
test_main.py::test_step7 PASSED
test_main.py::test_step8 PASSED
test_main.py::test_step9 PASSED
9 passed in 0.52s

$ python main.py     # exit code 0, prints every DataFrame
```

## "Not passed" troubleshooting (RESOLVED)

Bare `pytest` on the PATH is the pyenv shim (`~/.pyenv/shims/pytest`), which runs the
*system* Python 3.8.13. That interpreter had no pandas, so the suite died during
collection:

```
test_main.py:2: in <module>
    import pandas as pd
E   ModuleNotFoundError: No module named 'pandas'
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
```

Fix applied - pandas 2.0.3 + pytest 8.3.5 are now installed for every interpreter a
test runner might pick:

1. pyenv system Python 3.8.13 (`python3 -m pip install --user pandas==2.0.3 pytest==8.3.5`)
2. project `.venv` (`.venv/bin/python -m pip install pandas==2.0.3 pytest==8.3.5`)
3. pipenv virtualenv (`pipenv install`, `~/.local/share/virtualenvs/se_sql_select_lab-pX3ChyuT`)

Verified after the fix:

| command | result |
| --- | --- |
| `pytest` (system Python) | 9 passed |
| `.venv/bin/python -m pytest` | 9 passed |
| `pipenv run pytest` | 9 passed |
| `python3 main.py` | exit 0, 220 lines of DataFrame output |

## Notes

* Step 9 returns the original `orderDate` column followed by the `day`, `month` and
  `year` columns, as described in the README ("Return the original order date column
  followed by three new columns").
* Steps 2-9 run at import time (required by `test_main.py`), while the reference
  `employeeData` / `orderDetails` prints and `conn.close()` live under an
  `if __name__ == "__main__":` guard so that importing `main` never closes the
  connection or floods the test output.


