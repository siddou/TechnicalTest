# Deal super smart avec une boutique de vente de DVDs

- The code is written in Python 3 (Tested with Python 3.11.2)
- It uses regex to parse the file 'Back-to-the-Future.txt' to calculate the total price of a DVD order.
- It takes into account discounts on Back to the Future trilogy DVDs (10% for 2 different titles and 20% for 3 different).
- Replacement variables have been used throughout the script so that changes can be done easily.
- The function "test_calculate_total" verifies the expected result of 5 example cases.

## Start using the project

### Clone the project

```bash
git clone https://github.com/siddou/TechnicalTest
```

### Activate the VirtualEnv

```bash
cd TechnicalTest
python3 -m venv env
source env/bin/activate
```

### Install required packages

```bash
pip3 install -r requirements.txt
```

### Launch program

```bash
python3 dvdshop.py
```

### Launch test

```bash
python3 -m pytest dvdshop.py
```
