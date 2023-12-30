import os
import markdown
import glob
import shutil
from collections import OrderedDict
import parseconfig as pc

navbar_boilerplate = f"""\
    <nav>
        <ul class="menu">
            <li><a href="index.html">Home</a></li>
            <li><a href="{pc.config_dict['links']['resume']}">Resume</a></li>
            <li><a href="mailto:{pc.config_dict['links']['email']}">Contact</a><li>
        </ul>
        <hr>
    </nav>
"""
index_boilerplate = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{pc.config_dict['info']['name']}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {navbar_boilerplate}
    <img src="{pc.config_dict['info']['pic']}" style="max-width:20%;min-width:40px;float:right;border-radius: 50%;" alt="profile">
    <div>
        <h1>{pc.config_dict['info']['name']}</h1>
        <h3><em>{pc.config_dict['info']['sec']}</em></h3>
    </div>
    <p>{pc.config_dict['info']['desc']}</p>
    <h2>Activity</h2>
    <ul>
"""
footer_boilerplate = f"""
        <footer>
            <hr>
            <a href="https://github.com/ritzfy/blog-gen">copy, right?</a>
            |
            <a href="{pc.config_dict['links']['linkedin']}">linkedin</a>
            |
            <a href="{pc.config_dict['links']['github']}">github</a>
        </footer>
    </body>
</html>
"""
if not os.path.exists('gen'):
    os.makedirs('gen')

md_files = glob.glob('content/*.md')
date_title_dict = {}
for md_file in md_files:
    date = os.path.splitext(os.path.basename(md_file))[0]
    with open(md_file, 'r') as f:
        lines = f.readlines()
        title = lines[0].strip().lstrip('# ').rstrip()  # Get title from first line
        text = ''.join(lines)  # Get all the text including the title
        date_title_dict[date] = title
        print(f'{date}-{title}')

    html = markdown.markdown(text)
    html_file = "gen/" + os.path.basename(md_file).rsplit('.', 1)[0] + '.html'
    with open(html_file, 'w') as f:
        f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<title>' + title + '</title>\n')
        f.write('<link rel="stylesheet" href="style.css">\n</head>\n<body>\n')
        f.write(navbar_boilerplate)
        f.write(f'{html}\n')
        f.write(footer_boilerplate)

sorted_dict = OrderedDict(sorted(date_title_dict.items()))

with open('gen/index.html', 'w') as index:
    index.write(index_boilerplate + '\n')
    for date, title in sorted_dict.items():
            index.write(f'<li>{date} - <a href="{date}.html">{title}</a></li>\n')
    index.write(f'</ul>')
    index.write(f'{footer_boilerplate}')

shutil.copy2("static/style.css", "gen/")