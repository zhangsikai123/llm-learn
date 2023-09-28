lint:
	pre-commit run --all-files

fix:
	git add .
	git commit -m "$$(git status --porcelain)"
	make lint
test:
	python langchain/test_wrapper.py