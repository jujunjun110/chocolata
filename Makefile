install:
	virtualenv ENV
	( \
		source ENV/bin/activate; \
		pip install -r requirements.txt; \
		)

activate:
	source ./ENV/bin/activate
