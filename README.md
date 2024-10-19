# django-unicorn-examples

Simple examples for django-unicorn components.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Installation

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
