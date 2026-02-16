install:
	uv sync

brain-games:
	uv run VD_games

build:
	python3 -m build

lint:
	uv run ruff check .
package-install:
	uv tool install dist/*.whl

