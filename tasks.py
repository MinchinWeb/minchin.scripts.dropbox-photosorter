from pathlib import Path

from invoke import task

try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] minchin.releaser not available.")

try:
    from minchin.text import subtitle, title
except ImportError:
    subtitle = print
    title = print

REQUIREMENT_FILES = [
    "base",
    "dev",
]

ALL_REQUIREMENT_FILE = "all"

REQUIREMENTS_PATH = [
    ".requirements",
]


@task
def update(ctx, verbose=False):
    """
    Update python requirements files to latest versions.
    Also, rebuilds "all.in" requirement file.
    """
    title("Update python requirements files to latest versions")

    base_path = Path(".")
    for folder in REQUIREMENTS_PATH:
        base_path = base_path / folder
    print(f'** base path: "{base_path}"')

    all_requirements = base_path.resolve() / f"{ALL_REQUIREMENT_FILE}.in"
    # make sure file already exists
    all_requirements.touch()
    all_requirements.write_text(
        "# ** This file is automatically generated. **\n" "# Do not edit by hand\n" "\n"
    )
    with all_requirements.open("a") as all_requirements_file:
        for requirement in REQUIREMENT_FILES:
            print()
            subtitle(f"** {requirement} **")
            print()
            ctx.run(
                f"pip-compile {base_path / requirement}.in --upgrade", hide=not verbose
            )
            print(f"-r {requirement}.in", file=all_requirements_file)

    print()
    subtitle(f"** {all_requirements} **")
    print()
    ctx.run(
        f"pip-compile {base_path / ALL_REQUIREMENT_FILE}.in --upgrade", hide=not verbose
    )


@task
def upgrade(ctx, requirements_file="all", build=False, dev=False, verbose=False):
    """
    Upgrade python requirements to version specified in requirements files.
    """

    title("Upgrade python requirements to version specified in requirements files")

    if build is True:
        requirements_file = "build"
    elif dev is True:
        requirements_file = "dev"

    base_path = Path(".")
    for folder in REQUIREMENTS_PATH:
        base_path = base_path / folder
    requirements_file = base_path / f"{requirements_file}.txt"
    print(f"** requirements file: {requirements_file}")

    # run as a module, rather than the script, to all pip-tools to upgrade
    # itself on Windows
    ctx.run(f"python -m piptools sync {requirements_file.resolve()}", hide=not verbose)
