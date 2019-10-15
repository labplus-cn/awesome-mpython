BASEDIR=$(CURDIR)
DOCDIR=$(BASEDIR)/docs

install:
	pip install mkdocs mkdocs-material

link:
	ln -sf $(BASEDIR)/README.md $(DOCDIR)/index.md
	ln -sf $(BASEDIR)/Labplus.md $(DOCDIR)/Labplus.md

serve:
	$(MAKE) link
	mkdocs serve

deploy:
	$(MAKE) link
	mkdocs gh-deploy --clean