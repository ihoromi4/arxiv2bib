# Goal

The goal is to create a Python CLI utility named `arxiv2bib`.

This utility should:

*   Accept an `arXiv ID` as input.
*   Automatically find the corresponding publication in a peer-reviewed journal.
*   Return a BibTeX record (for either the published or the arXiv version).
*   Display the search steps to the user.

The expected outcome is a working CLI tool (`arxiv2bib <id>`), an open-source Python package with a `pyproject.toml` file, along with tests and documentation.

# Tasks

- [ ] **Phase 1: Project Setup & Core Logic**
    - [x] 1.1. Initialize project structure and dependencies.
    - [ ] 1.2. Implement core functionality for fetching data from arXiv.
    - [ ] 1.3. Implement core functionality for fetching data from CrossRef.
    - [ ] 1.4. Add BibTeX generation logic.
- [ ] **Phase 2: CLI & User Interface**
    - [ ] 2.1. Create the command-line interface using `click` python library.
    - [ ] 2.2. Implement user-facing logging to show search steps.
- [ ] **Phase 3: Testing & Refinement**
    - [ ] 3.1. Write unit and integration tests.
    - [ ] 3.2. Add optimizations like caching and error handling.
- [ ] **Phase 4: Documentation & Publication**
    - [ ] 4.1. Create a comprehensive `README.md` file.
    - [ ] 4.2. Prepare the package for publication.
