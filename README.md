# The Phenomenon EPUB generator

## Usage

Get HTML from [the Phenomenon Compiler](https://grovejay.github.io/Phenomenon_Compiler/index.html) and save it into a file `full.html`.

Prepare the environment:

```
mkvirtualenv .env
pip install -r requirements.txt
```

Generate ePUB:

```
./make-epub.py
```

Read resulting `test.epub` in a reader of your choice.
