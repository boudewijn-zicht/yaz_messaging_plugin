init:
    pip3 install -r requirements.txt

test:
    nosetests --with-coverage --cover-html --cover-package yaz_messaging_plugin

upload: test
	python setup.py sdist upload -r pypi

.PHONY: init test upload
