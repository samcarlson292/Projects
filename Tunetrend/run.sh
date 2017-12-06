#! /bin/sh

echo "Calling get_related.py"
python get_related.py
echo "Done get_related.py"
echo "Calling load_artists.py"
python load_artists.py
echo "Done load_artists.py"
echo "Calling get_songs.py"
python get_songs.py
echo "Done get_songs.py"
echo "Calling load_songs.py"
python load_songs.py
echo "Done load_songs.py"

echo "DONE"
