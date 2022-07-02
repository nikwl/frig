# frig 
Figure cReation Is God-awful

## Installation 
```bash
pip install git+https://github.com/nikwl/frig.git
```

## Use
(1) Automatically strip whitespace from all images in a directory. New images are dumped into a `stripped` subdirectory.
```
python -m frig.strip dir/to/strip
```

(2) Automatically convert any vectorized image to pdf. Designed for use on windows but should work on any OS. New pdfs are dumped into a `pdfized` directory.
```
python -m frig.pdfize dir/to/pdfize
```
Requires inkscape to be installed. If it's installed in a non-standard location, set the environment variable `INKSCAPE_PATH`.
```
$env:INKSCAPE_PATH = 'C:\\Program Files\\Inkscape\\bin\\inkscape.exe'
```

