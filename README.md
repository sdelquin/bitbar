# BitBar

Different applications to work with [BitBar](https://github.com/matryer/bitbar).

## Plugin Folder

BitBar needs to set a **Plugin Folder** where to load scripts from. I usually set it to `~/.bitbar` and there I leave bash scripts like `<plugin>.sh` with the following structure:

```bash
#!/bin/bash

source ~/.virtualenvs/<plugin>/bin/activate
python ~/path/to/plugin/main.py
```
