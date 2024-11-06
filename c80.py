import os
import subprocess
import sys
import shlex

def run_command(command, *args):
    """Helper function to run system commands."""
    try:
        subprocess.run([command] + list(args), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
    except FileNotFoundError:
        print(f"Command not found: {command}")

def assoc(args):
    run_command("assoc", *args)

def attrib(args):
    run_command("attrib", *args)

def break_cmd(args):
    print("BREAK command doesn't require arguments; it handles CTRL+C checking in CMD.")

def bcdedit(args):
    run_command("bcdedit", *args)

def cacls(args):
    run_command("cacls", *args)

def call(args):
    print("CALL command can be used only in batch files to call another batch file.")

def cd(args):
    """Change the current directory to the specified path, or to home if empty."""
    if args:
        if args[0] == "":
            os.chdir(os.path.expanduser("~"))  # Change to home directory if empty string
        else:
            os.chdir(args[0])
    else:
        print(os.getcwd())

def chcp(args):
    run_command("chcp", *args)

def chdir(args):
    cd(args)

def chkdsk(args):
    run_command("chkdsk", *args)

def chkntfs(args):
    run_command("chkntfs", *args)

def cls(args):
    os.system("cls")

def cmd(args):
    os.system("cmd")

def color(args):
    run_command("color", *args)

def comp(args):
    run_command("comp", *args)

def compact(args):
    run_command("compact", *args)

def convert(args):
    run_command("convert", *args)

def copy(args):
    run_command("copy", *args)

def date(args):
    run_command("date", *args)

def del_cmd(args):
    run_command("del", *args)

def dir_cmd(args):
    run_command("dir", *args)

def diskpart(args):
    run_command("diskpart", *args)

def doskey(args):
    run_command("doskey", *args)

def driverquery(args):
    run_command("driverquery", *args)

def echo(args):
    print(" ".join(args))

def endlocal(args):
    print("ENDLOCAL is used in batch scripts to end localization of environment variables.")

def erase(args):
    del_cmd(args)

def exit_cmd(args):
    sys.exit(0)

def fc(args):
    run_command("fc", *args)

def find(args):
    run_command("find", *args)

def findstr(args):
    run_command("findstr", *args)

def format(args):
    run_command("format", *args)

def gpresult(args):
    run_command("gpresult", *args)

def hostname(args):
    """Displays the computer's hostname."""
    run_command("hostname")

def ipconfig(args):
    """Displays network configuration information."""
    run_command("ipconfig", *args)

def ping(args):
    """Pings a specified host."""
    if args:
        run_command("ping", *args)
    else:
        print("Usage: ping <host>")

def python(args):
    """Runs a Python script or starts the interactive Python shell."""
    if args:
        run_command("python", *args)  # Run a Python script
    else:
        os.system("python")  # Start the Python interactive shell

def help_cmd(args):
    commands = [
        "ASSOC", "ATTRIB", "BREAK", "BCDEDIT", "CACLS",
        "CALL", "CD", "CHCP", "CHDIR", "CHKDSK",
        "CHKNTFS", "CLS", "CMD", "COLOR", "COMP",
        "COMPACT", "CONVERT", "COPY", "DATE", "DEL",
        "DIR", "DISKPART", "DOSKEY", "DRIVERQUERY", "ECHO",
        "ENDLOCAL", "ERASE", "EXIT", "FC", "FIND",
        "FINDSTR", "FORMAT", "GPRESULT", "HELP", "TITLE",
        "FOR", "FSUTIL", "FTYPE", "GOTO", "GRAFTABL",
        "ICACLS", "IF", "LABEL", "MD", "MKDIR",
        "MKLINK", "MODE", "MORE", "MOVE", "OPENFILES",
        "PATH", "PAUSE", "POPD", "PRINT", "PROMPT",
        "PUSHD", "RD", "RECOVER", "REM", "REN",
        "RENAME", "REPLACE", "RMDIR", "ROBOCOPY", "SET",
        "SETLOCAL", "SC", "SCHTASKS", "SHIFT", "SHUTDOWN",
        "SORT", "START", "SUBST", "SYSTEMINFO", "TASKLIST",
        "TASKKILL", "TIME", "TASKMGR", "CONTROL", "TREE",
        "TYPE", "VER", "VERIFY", "VOL", "XCOPY", "WMIC",
        "EXE", "HOSTNAME", "IPCONFIG", "PING", "PYTHON"  # Added new command
    ]
    
    if args:
        command = args[0].upper()
        if command in commands:
            run_command("cmd", "/c", "help", command)
        else:
            print(f"No help available for: {command}")
    else:
        print("Available commands:")
        for command in commands:
            print(f" - {command}")

def exe(args):
    """Opens an executable file."""
    if args:
        run_command(args[0])  # Open the executable
    else:
        print("Usage: exe <path_to_executable>")

def taskmgr(args):
    """Opens the Task Manager."""
    os.system("taskmgr")

def control_panel(args):
    """Opens the Control Panel."""
    os.system("control")

def title(args):
    if args:
        os.system(f"title {' '.join(args)}")
    else:
        print("Current title is:", os.get_terminal_size())

def main():
    # Set the title to "c80" when the program starts
    title(["c80"])
    
    # Display the main header
    print("Command Line Interface 80 [Made by ZipSaf]")
    
    while True:
        current_directory = os.getcwd()
        user_input = input(f"{current_directory}---> ").strip()
        
        # Use shlex.split to handle quoted paths
        parsed_input = shlex.split(user_input)
        command = parsed_input[0].lower()
        args = parsed_input[1:]

        if command == "exit":
            exit_cmd(args)
        elif command == "help":
            help_cmd(args)
        elif command == "title":
            title(args)
        elif command == "cd":
            cd(args)
        elif command == "cls":
            cls(args)
        elif command == "echo":
            echo(args)
        elif command == "dir":
            dir_cmd(args)
        elif command == "md" or command == "mkdir":
            run_command("mkdir", *args)
        elif command == "taskmgr":
            taskmgr(args)
        elif command == "control":
            control_panel(args)
        elif command == "exe":
            exe(args)
        elif command == "hostname":
            hostname(args)
        elif command == "ipconfig":
            ipconfig(args)
        elif command == "ping":
            ping(args)
        elif command == "python":
            python(args)
        # Add more command handling as needed
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
