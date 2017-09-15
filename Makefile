install:
	virtualenv ENV
	( \
		source ENV/bin/activate; \
		pip install -r requirements.txt; \
		)

black:
	ls ./movie_materials | xargs sh ./do.sh
