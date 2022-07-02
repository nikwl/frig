# frig 
Figure cReation Is God-awful

## Installation 
```bash
pip install git+https://github.com/nikwl/frig.git
```

## Use
(1) Automatically remove whitespace from all images in a directory. New images are dumped into a `cropped` subdirectory.
```
python -m frig.crop dir/to/crop
```

(2) Convert any vectorized image to svg. Designed for use on windows but should work on any OS. 
```
python -m frig.convert_pdf dir/to/pdf-ize
```