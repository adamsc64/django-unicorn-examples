# django-unicorn-examples

Simple examples for django-unicorn components.

## Setup

### Development via VSCode

To set up your development environment in Visual Studio Code:

1. **Open the Project**:
   - Open the project folder in VSCode.

1. **Set Up Virtual Environment**:
   - Create a virtual environment by running `python3 -m venv .venv` in the terminal.
   - Activate the virtual environment with `source .venv/bin/activate`.

1. **Select Python Interpreter**:
   - Open the Command Palette (`Cmd+Shift+P` on Mac or `Ctrl+Shift+P` on Windows/Linux).
   - Choose `Python: Select Interpreter` and select the interpreter from the `.venv` folder.

1. **Launch Configuration**:
   - A `launch.json` file is included in the `.vscode` folder. This file is pre-configured for debugging.
   - To start debugging, go to the Debug view (`View > Run` or `Cmd+Shift+D`), select the `Django app` configuration, and click the green play button.

1. **Start Debugging**:
   - The debugger will start the Django development server. You can set breakpoints and use other debugging features as needed.

### Development via Docker Compose

#### Prerequisites

- Docker
- Docker Compose

1. Clone the repository:

    ```sh
    git clone https://github.com/adamsc64/django-unicorn-examples.git
    cd django-unicorn-examples
    ```

2. Build the Docker images:

    ```sh
    docker compose build
    ```

### Run Migrations

To apply the database migrations, run:

```sh
docker compose run web python manage.py migrate
```

### Serve the App

```sh
docker compose up
```

The app will be available at `http://localhost:8000`.
