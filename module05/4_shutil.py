from shutil import make_archive, unpack_archive

make_archive(
    "archive1", "gztar", root_dir="."
)  # create archive, format gztar, root_directory
unpack_archive(
    "archive1.tar.gz", extract_dir="4_shutil"
)  # name archive with format and name extract_directory
