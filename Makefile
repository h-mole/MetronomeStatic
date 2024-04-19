build-wheel:
	python setup.py bdist_wheel

lint:
	pylint --rcfile=.pylintrc PyBirdViewCode

test:
	pytest -s

test-cov:
	pytest -s --cov-report=term-missing \
		--cov=PyBirdViewCode/clang_utils \
		--cov=PyBirdViewCode/utils

test-eval-cov:
	pytest -s tests/test_clangutils/code_evals --cov-report=term-missing \
		--cov=PyBirdViewCode/clang_utils/code_eval

format:
	autoflake -r --in-place --remove-unused-variables \
		--remove-all-unused-imports --exclude=__init__.py PyBirdViewCode demos tests
	isort -rc PyBirdViewCode demos tests
	black .