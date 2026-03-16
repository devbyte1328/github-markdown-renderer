

# Github Markdown Renderer

This repository provides a setup to render GitHub-styled Markdown documents

locally (offline) with mdBook.

---

## Installation

```
sudo pacman -S mdbook --noconfirm && \
git clone https://github.com/devbyte1328/github-markdown-renderer && \
cd github-markdown-renderer && \
python Setup.py && \
cd .. && \
rm -rf github-markdown-renderer && \
source ~/.bashrc
```

---

## Usage

Render a Markdown file with:

```
markdown README.md
```

Then open:

```
http://localhost:4000
```


