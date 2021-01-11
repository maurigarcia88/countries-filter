## User guide
### Install packages
```
sudo apt install git
sudo apt install python3-pip
sudo apt-get install python3-venv
```

### Create folders and download repository

```
mkdir mgarcia-challenge
cd mgarcia-challenge
git clone https://github.com/maurigarcia88/countries-filter.git
cd countries-filter
```
### Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run API
Run the live server in a terminal
```
uvicorn main:app --reload
```
Go to <http://127.0.0.1:8000/docs>
Click on first GET tab, then on Try it out.

Add required values.

You may want to use additional endpoints
