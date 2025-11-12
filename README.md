# Bread Scaler

Usage: `python3 bread.py --dough-weight 900 --water 80 --salt 2 --starter 12`

Provide the total dough weight of a dough ball in grams, and the remaining ingredients in baker's percentages: https://www.kingarthurbaking.com/pro/reference/bakers-percentage

What you'll get is a recipe for a single doughball with the ingredients displayed in grams:
```
python3 bread.py -d 900 -w 80 -s 2 --starter 12
Number of dough balls: 1

Recipe:
Flour: 435.16g
Water: 336.26g
Salt: 9.89g
Starter: 118.68g
```

You can scale the recipe to multiple loaves if you'd like with the `--quantity` flag. Lastly, don't think of this as a bread-only tool, you can use this for pizza dough as well:

```
python3 bread.py -d 250 -w 72 -s 2.6 --starter 15 -q 3
Number of dough balls: 3

Recipe:
Flour: 365.12g
Water: 244.85g
Salt: 11.17g
Starter: 128.87g
```

The script defaults to using a starter that's equal parts flour and water, however if you feed a starter that's (for example) 1:4:5 (one part levain to 4 parts water to 5 parts flour), you can account for this by using the `--ratio` flag and providing the percentage of water as a float, in this case, `.8`

If your recipe uses sugar, oil or commercial yeast, you can pass in `--sugar`, `--oil` or `--yeast`.

If you like round numbers, use the `--round` flag to round the displayed ingredients to the nearest half gram.

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