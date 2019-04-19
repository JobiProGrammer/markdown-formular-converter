# Mathjax/Latex Formular Markdown Syntax to Github Compatible Converter

## Functionality
In most markdown interpreters nowadays you can use the dollar sign syntax to write math formulars in a latex style. For example: $E = mc^2$ would become ![equation](https://latex.codecogs.com/gif.latex?E%20%3D%20mc%5E2). Sadly, Github does not support this feature in their markdown interpreter. So, a workaround to still be able to use formulars in your Github repo's readme file is to replace them with images as suggested in this [stackoverflow](https://stackoverflow.com/questions/12502440/markdown-formula-display-in-github) answer.

For Example [codecogs](https://www.codecogs.com/latex/about.php) can be used for this which is an online mathjax compiler that can return an image of the formular. This can than be embedded into the markdown file.
The problem is that you have to encode the latex string into a url-friendly format and doing this can be a lot of work if you have a lot of formulars.

This simple converter which is written in python is meant to solve this problem: It automatically detects latex formatted formulars (marked with $$ and inline with $) and replaces them with a markdown image that points to the url of codecogs.

## Requirements
The python package `click` is required to run the code. It is installable with `pip3 install click`

## Usage
`python3 github_markdown.py -p README_with_latex.md -n README.md`

* `-p` is the path of the markdown file which uses mathjax/latex formular syntax
* `-n` is the path of the new file

