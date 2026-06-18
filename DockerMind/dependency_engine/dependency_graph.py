dependencies = {

    "frontend": ["backend"],

    "backend": ["postgres"],

    "postgres": []
}


def get_dependencies(service):

    return dependencies.get(
        service,
        []
    )


if __name__ == "__main__":

    for service in dependencies:

        print(
            service,
            "->",
            get_dependencies(service)
        )