# Bread Scaler

Usage: `python3 bread.py --dough-weight 900 --water 80 --salt 2 --starter 12`

What you'll get is a recipe for a single doughball with the ingredients displayed in grams:
```
python3 bread.py -d 900 -w 80 -s 2 -y 12
Number of dough balls: 1

Recipe:
Flour: 435.6g
Water: 336.6g
Salt: 9.9g
Starter: 118.8g
```

You can scale the recipe to multiple loaves if you'd like with the `--quantity` flag. Lastly, don't think of this as a bread-only tool, you can use this for pizza dough as well:

```
python3 bread.py -d 250 -w 72 -s 2.6 -y 15 -q 3
Number of dough balls: 3

Recipe:
Flour: 364.65g
Water: 244.53g
Salt: 11.15g
Starter: 128.7g
```

### Testing

Make sure to start a virtual environment:
`python3 -m venv .venv`

Then start it:
`source .venv/bin/activate`

And install the requirements:
`pip install -r requirements.txt`

Then you can run `pytest` to run tests. For those new to venv, run `deactivate` to stop your virtual 
environment.

### Code Coverage:
`pytest --cov --cov-report=html:bread_cov`