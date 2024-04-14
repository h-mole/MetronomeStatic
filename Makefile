build-wheel:
	python setup.py bdist_wheel

lint:
	pylint --rcfile=.pylintrc MetronomeStatic

test:
	pytest -s

test-cov:
	pytest -s --cov-report=term-missing \
		--cov=MetronomeStatic/clang_utils \
		--cov=MetronomeStatic/utils

test-eval-cov:
	pytest -s tests/test_clangutils/code_evals --cov-report=term-missing \
		--cov=MetronomeStatic/clang_utils/code_eval

format:
	autoflake -r --in-place --remove-unused-variables \
		--remove-all-unused-imports --exclude=__init__.py MetronomeStatic demos tests
	isort -rc MetronomeStatic demos tests
	black .