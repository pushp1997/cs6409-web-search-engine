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

```bash

```