# Goal

The goal is to create a Python CLI utility named `arxiv2bib`.

This utility should:

*   Accept an `arXiv ID` as input.
*   Automatically find the corresponding publication in a peer-reviewed journal.
*   Return a BibTeX record (for either the published or the arXiv version).
*   Display the search steps to the user.

The expected outcome is a working CLI tool (`arxiv2bib <id>`), an open-source Python package with a `pyproject.toml` file, along with tests and documentation.

# Rules

- Follow these rules strictly.
- Do not move to the next task until user ask to do that.

# Project State

- The `uv` package panager is used.
- The virtual environment `.venv` already exists.
- The `main.py` is entry point of the project.
- The logic code is placed in `arxiv2bib` directory.

# Tasks

- [x] 1. Project Setup
    - [x] 1.1. Initialize project structure and dependencies.
- [x] 2. CLI & User Interface
    - [x] 2.1. Create the command-line interface using `click` python library.
    - [x] 2.2. Implement user-facing logging to show search steps with placeholder phrases.
- [ ] 3. Core Logic
    - [x] 3.1. Implement core functionality for fetching data from arXiv.
    - [ ] 3.2. Implement core functionality for fetching data from CrossRef.
    - [ ] 3.3. Add BibTeX generation logic.
- [ ] 4. Testing & Refinement
    - [ ] 4.1. Write unit and integration tests.
    - [ ] 4.2. Add optimizations like caching and error handling.
- [ ] 5. Documentation & Publication
    - [ ] 5.1. Create a comprehensive `README.md` file.
    - [ ] 5.2. Prepare the package for publication.
