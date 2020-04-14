# git.ir Video Downloader
Downloads video files from scattered links throughout a git.ir page.

> Note: Only for freely available video.


## Installing:

### Installation Requirements:
- Python >= 3.6
- pipx

```bash
$ pip install pipx
```

```bash
$ pipx install gitir-download
```

## Usage:

All the files will be downloaded inside a custom folder based on the URL.

```bash
$ gid <git.ir_url>
```

To create a user defined function, use the `--name` flag.

```bash
$ gid <git.ir_url> --name 'Python Scripting'
```
