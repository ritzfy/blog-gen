# blog-gen
Stupidly simple blog generation script with support for classless CSS

## Directory Structure
- `assets`, stores images, documents etc
- `content`, stores md files in the `YYYY-MM-DD.md` format
- `gen`, generated html

## Requirements
`python`, `markdown` which uses John Gruber's implementation of markdown

clone the repo and and run `rm -rf assets/* content/* gen/*` to clean the directories so you can put your own stuff
Input your own details in config.ini and just run, 
```bash
python gen.py
```
