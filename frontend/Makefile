.PHONY: check
check:
	poetry run black .
	poetry run isort .
	poetry run flake8 .
	echo 'All checks passed successfully'