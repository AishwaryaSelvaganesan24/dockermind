dependencies = {

    "frontend": ["backend"],

    "backend": ["postgres"],

    "postgres": []
}


def get_affected_services(root_pod):

    affected = []

    def dfs(target):

        for service, deps in dependencies.items():

            if target in deps and service not in affected:

                affected.append(service)

                dfs(service)

    dfs(root_pod)

    return affected


if __name__ == "__main__":

    print(
        get_affected_services(
            "postgres"
        )
    )