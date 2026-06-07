# visual-studio

[![CodSpeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://app.codspeed.io/MatusRyba/visual-studio?utm_source=badge)

A small collection of Python utilities:

- `flag_generator.py` — generates a flag image with Pillow and displays it in a Tkinter canvas.
- `sort_names.py` — sorts a list of values.

## Benchmarks

Performance is tracked continuously with [CodSpeed](https://codspeed.io). Benchmarks live in `benchmarks/` and use `pytest-codspeed`.

Run them locally with:

```bash
uv run pytest benchmarks/ --codspeed
```
