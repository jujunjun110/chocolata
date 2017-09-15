if [ $# -ne 1 ]; then
  echo "require single filename" 1>&2
  exit 1
fi

filename=$1

cd ./
mkdir images && mkdir chromakey

ffmpeg -i ./movie_materials/${filename} -vcodec png -r 30 images/image_%05d.png
python main.py
ffmpeg -framerate 30 -i chromakey/image_%05d.png -vcodec libx264 -pix_fmt yuv420p -r 30 ./movie_results/${filename}

rm -rf images && rm -rf chromakey
