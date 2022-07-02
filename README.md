# frig 
Figure cReation Is God-awful (on Windows).

## Installation 
```bash
pip install git+https://github.com/nikwl/frig.git
```

## Use
(1) Automatically remove whitespace from all images in a directory. New images are dumped into a `stripped` subdirectory.
```
python -m frig.strip dir/to/strip
```

(2) Convert all vectorized images in a directory to pdf. Designed for use on windows but should work on any OS. New pdfs are dumped into a `pdfized` directory.
```
python -m frig.pdfize dir/to/pdfize
```
Requires inkscape to be installed. If inkscape is installed in non-standard location use the INKSCAPE_PATH environment variable to point to it.
```
$env:INKSCAPE_PATH = 'C:\\Program Files\\Inkscape\\bin\\inkscape.exe'
```
