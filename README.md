# Instructions

## Pre-Requisites

Ensure you do this.

1. Run and export the model using the `SummerizationModel.ipynb` notebook.

## Build Image and Container

1. `docker build -t text-summerization-app .`
2. `docker run -d --name text-summerization-app --mount type=bind,source="$(pwd)",target=/app -p 8888:8888 -p 5001:5000 text-summarization-app`

This builds an image called text-summerization-app and uses that to create a container, exposing ports 8888 and 5000 (mapped to port 5001).

use `docker logs text-summerization-app` to get the link for the notebook, and go to `127.0.0.1:5001` to access the flask webapp.

-   `docker stop text-summerization-app` to stop the container
-   `docker start text-summerization-app` to start the app again

## Dev Setup

1. `python -m venv venv`
2. `source ./venv/bin/activate` or `venv\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`

### VSCode Task
- `CTRL + SHIFT + P` -> `Tasks: Run Task` -> `Build`
Runs the `Build` task, which calls the `build` script.

# Contributing
## Conventional Commits

We adhere to the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification to make our commit history more readable and to automate the versioning process. Each commit message should be structured as follows:

```markdown
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The main types are:

- `feat`: a new feature
- `fix`: a bug fix
- `docs`: documentation only changes
- `style`: changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: a code change that neither fixes a bug nor adds a feature
- `test`: adding missing tests or correcting existing tests
- `build`: changes to the build process or auxiliary tools and libraries such as documentation generation

## Code Quality Tools

Before submitting any changes, ensure your code passes all quality checks. We use several tools to maintain code quality and consistency. Run the `build.sh` script located at the project's root directory. This script will execute the following tools on the `src` and `tests` directories:

- [**Black**](https://black.readthedocs.io/en/stable/?badge=stable): An uncompromising code formatter that adheres to PEP 8 style guide.
- [**Pylint**](https://pylint.readthedocs.io/en/latest/): A tool that looks for programming errors, helps enforce a coding standard, and sniffs for code smells.
- [**Pytest](https://docs.pytest.org/en/8.0.x/) / [Pytest-Cov**](https://pytest-cov.readthedocs.io/en/latest/): A framework that makes it easy to write simple tests, yet scales to support complex functional testing. The `pytest-cov` plugin is used for measuring code coverage.

To run the script, navigate to your project's root directory and execute: `source ./scripts/build.sh` on Mac or `.\scripts\build.ps1` on windows.

Ensure that: 
- Black reformats your code with no errors.
- Pylint shows no errors or warnings. Pay attention to the feedback and correct your code as necessary.
- All your tests pass with Pytest.
- Your code coverage does not decrease. Aim to cover as much of your - code with tests as possible.
