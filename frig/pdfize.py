import os
import argparse
import subprocess


def convert(path, ext):
    exe = os.environ.get(
        'INKSCAPE_PATH',
        r"C:\Program Files\Inkscape\bin\inkscape.exe"
    )
    export_type = r"--export-type={}".format(ext)
    cmd = [
        exe,
        export_type,
        path,
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, err = proc.communicate()
    if not err:
        print("Processed {}".format(path))
    else:
        print('--Error--\n', err.decode())


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="")
    arg_parser.add_argument(
        "dir",
        type=str,
        help="directory to convert"
    )
    arg_parser.add_argument(
        "--ext",
        default=".svg",
        type=str,
        help="extension"
    )
    args = arg_parser.parse_args()
    if not args.ext[0] == ".":
        args.ext = "." + args.ext
    assert os.path.isdir(args.dir)
    for p in os.listdir(args.dir):
        if os.path.splitext(p)[-1] == args.ext:
            convert(
                os.path.abspath(os.path.join(args.dir, p)),
                ext="pdf",
            )
