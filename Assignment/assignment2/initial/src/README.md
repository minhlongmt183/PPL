# PPL Toolkit

## Assigment 2
Generate *ASTGenSuite.py**:
- 1. Change ASTGeneration.py visitProgram():
    `return Program(...)` **-->** `return [Program(...)]`
- 2. `python3 run.py test ASTGenSuite`
- 3. `python3 toolkit.py`

Notes:
- Use `--fix-index` to fix your output index (output will begin at 300)
- Please clean up test folder before run:
    ```
    rm test/solutions/*
    rm test/testcases/*
    ```