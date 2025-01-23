This repo demonstrates a bug in the pydantic.mypy plugin in a complicated
case (modeling a node graph) with a base class that includes `extra='forbid'`

to run this example:

```sh
git clone https://github.com/tlambert03/pydantic-mypy-err.git
cd pydantic-mypy-err

pip install mypy==1.14.1 pydantic==2.10.5
mypy example.py
```

false positive error observed:

```sh
example.py:3: error: Unexpected keyword argument "name" for "Square"  [call-arg]
Found 1 error in 1 file (checked 1 source file)
```
