install:
	virtualenv ENV
	( \
		source ENV/bin/activate; \
		pip install -r requirements.txt; \
		)

proccess-create-black-video: images black libx264
proccess-create-alpha-video: images alpha rawvideo

images:
	-mkdir images
	ls ./movie_materials | xargs -IARG ffmpeg -i ./movie_materials/ARG -vcodec png -r 30 images/ARG_%05d.png

black:
	python main.py black

alpha:
	python main.py alpha

libx264:
	$(MAKE) video CODEC=libx264 FMT=yuv420p

rawvideo:
	$(MAKE) video CODEC=prores_ks FMT=argb

video:
	ls ./movie_materials | xargs -IARG ffmpeg -framerate 30 -i chromakey/ARG_%05d.png -vcodec $(CODEC) -pix_fmt $(FMT) -r 30 ./movie_results/ARG

.PHONY: images black alpha libx264 rawvideo video
