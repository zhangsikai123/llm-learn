lint:
	pre-commit run --all-files

fix:
	git add .
	git commit -m "$$(git status --porcelain)"
	make lint
	git push
test:
	python -m sky_langchain.test_wrapper
