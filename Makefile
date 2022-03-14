
.PHONY: dist
dist:
	@rm -rf dist
	@python3 setup.py sdist bdist_wheel

.PHONY: install
install:
	@python3 setup.py install --record uninstall.txt

.PHONY: install-user
install-user:
	@python3 setup.py install --user

.PHONY: upload
upload: dist
	@twine upload --skip-existing dist/*

