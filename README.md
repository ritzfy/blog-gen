# blog-gen
Stupidly simple blog generation script with support for classless CSS

## Directory Structure
- `assets`, stores images, documents etc
- `content`, stores md files in the `YYYY-MM-DD.md` format
- `gen`, generated html

## Requirements and Usage
`python`, `markdown` which uses John Gruber's implementation of markdown

clone the repo and and run `rm -rf assets/* content/* gen/*` to clean the directories so you can put your own stuff
a basic classless stylesheet is there in `static/`, do modify it as per your needs

Input your own details in config.ini and just run, 
```bash
python gen.py
```
