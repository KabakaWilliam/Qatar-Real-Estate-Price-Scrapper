# Real Estate Price Index Qatar Scrapper

This script will scrape data from Qatar Central Bank and return a CSV of the current Real Estate Price Index data.

## To Run:

To run this script, install the required libraries:

```bash
$ pip3 install requirements.txt
```

Then run this main file:

```bash
$ python3 mainScrapper.py
```

This will save a CSV of the current index data in a directory called `IndexData`. The data will be in the format `RIPIQ_CURRENTDATE.csv`

To observe the exploration process look at the notebook `explore.ipynb` where I examine the different methods to find this data.

## Future Improvements

[] Turn this scrapper to an API that returns data
