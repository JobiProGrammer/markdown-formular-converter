import click
import urllib
from urllib.parse import quote


def change_char(s, p, r, skip_num=1):
    return s[:p]+r+s[p+skip_num:]

@click.command()
@click.option("-p", "--path", type=str, required=True, help="Path to the markdown file that should be converted")
@click.option("-n", "--new", required=True, type=str, help="Path to the new file")
def cli(path: str, new: str):
    with open(path, "r") as f:
        content = f.read()
    #content = list(content)

    found = content.find("$$")
    while found != -1:
        content = change_char(content, found, "", 2)
        found2 = content.find("$$")
        formular = content[found:found2]
        parsed = quote(formular)
        new_f = "![equation](https://latex.codecogs.com/gif.latex?{})".format(parsed)
        #new_f = '<img style="vertical-align: middle;" src="https://latex.codecogs.com/gif.latex?{}">'.format(parsed)
        content = content[:found] + new_f + content[found2+2:]
        found = content.find("$$")
    
    found = content.find("$")
    while found != -1:
        content = change_char(content, found, "")
        found2 = content.find("$")
        formular = content[found:found2]
        parsed = quote(formular)
        new_f = "![equation](https://latex.codecogs.com/gif.latex?{})".format(parsed)
        # the following comment out line can vertically align the intext formulars but won't work on github
        #new_f = '<img style="vertical-align: middle;" src="https://latex.codecogs.com/gif.latex?{}">'.format(parsed)
        content = content[:found] + new_f + content[found2+1:]
        found = content.find("$")


    with open(new , "w") as f:
        f.write(content)




if __name__ == "__main__":
    cli()
