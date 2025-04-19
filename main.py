from click import Group
from cli.commands import practice, history

def main():
    cli = Group()
    cli.add_command(practice)
    cli.add_command(history)
    cli()

if __name__ == "__main__":
    main()