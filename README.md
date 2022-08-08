This is some python scripting business I did for fun. I basically scraped a website of ladder data for StarCraft 2, cleaned up the data a bunch, then did some rudimentary data visualization and analysis on it.

I wouldn't recommend running scrape.py anymore since SC2's API has been broken for a while now and the site I scraped the data from hasn't been updated with a full dataset as a result. The data I have is basically the last full set of data available.

If you do want to run all of this on your own, you have to do the following:
* run `scrape.py`
* run `combine.py`
* run `broken.py`, which fixes a text encoding issue caused by the webscraper not handling certain unicode characters correctly
* move the CSVs to the `data` directory
* use `jupyter notebook` to run the python notebook (or if you use the jupyter notebook extension in VS Code, run it in there). Note that you need to have the `pandas`, `seaborn`, and `matplotlib` modules installed to run the contents of the notebook.