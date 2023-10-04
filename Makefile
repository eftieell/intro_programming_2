.PHONY: build serve publish
build:
	mdbook build
	cp js/searcher-pyscript.js docs/searcher.js

serve:
	mdbook serve

publish:
	rsync -ravP docs/* intropython@linux.cs.du.edu:~/public_html/intro-to-programming-2
