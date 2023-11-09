## Making virtual environment
```bash
python3 -m venv venv # First venv is the module, and second one is the name of the virtual environment
# or
virtualenv venv # needs to be installed globally
# or
python -m venv venv
```
## Activating virtual environment
### Windows
```bash
venv\Scripts\activate.bat
# or
venv\Scripts\activate.ps1
# or
venv\Scripts\activate
```
You may face some errors. Just Google it.
### Linux / macOS
```bash
source venv/bin/activate
```
### For install modules
```bash
pip install <package-name>
```
### Eqxporting requirements
```bash
pip freeze > requirements.txt
```
