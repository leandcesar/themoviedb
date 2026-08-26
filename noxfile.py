import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14"])
def tests(session: nox.Session) -> None:
    session.install("-r", "requirements-test.txt")
    session.run("python", "-m", "pytest", *session.posargs)
