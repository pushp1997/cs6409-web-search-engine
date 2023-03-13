# Mini Web Search Engine

```
By: Pushp Vashisht
MSc Computing Science
Student ID: 122102735
```

## Steps to run this program

### 1. Install the dependencies

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### 2. Run the Scraper

```bash
$ scrapy crawl wikipedia
```

### 3. Index the scraped documents

Make sure to remove "index/" folder from the project director if it exists.

```bash
$ python indexer.py
```

### 4. Run sample queries on the indexed documents

Add your queries to the `queries` list in `query.py`. For sample these queries have been written:
* "cork city"
* "aerlingus"
* "ireland"
* "india"

```bash
$ python query.py
```

Surprisingly, even if the starting point of the crawler was a wikipedia page for Cork City,
but search term "india" came out with a better score during testing.