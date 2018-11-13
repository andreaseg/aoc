from os import listdir, path
import subprocess
from colorama import Fore, Style, init as colorama_init

def print_warn(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

def print_err(message):
    print(Fore.RED + message + Style.RESET_ALL)

def print_ok(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def test_file(filename):

    exe = filename + ".exe"

    build = subprocess.Popen("fasm " + filename + ".asm " + exe, stdout=subprocess.DEVNULL)
    build.wait()

    print("Running " + filename + ".asm tests")

    for line in open(filename + ".test", 'r'):
        line = line.rsplit("=>", 1)
        if len(line) != 2:
            print("  Malformed test")
            continue
        args = line[0]
        expected_result = line[1]

        try:
            process = subprocess.Popen(exe, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            process.communicate(args)
            process.wait()
            process_result = process.stdout.readline()
        except subprocess.CalledProcessError as error:
            print_err("  Error: " + str(error.output))
        except:
            print_err("  " + exe + " is not valid application")
            return

        if process_result == expected_result:
            print_ok("  Test succeded")
        else:
            print_warn("  Test failed")


def main():

    colorama_init()

    asm_files = [f[:-4] for f in listdir() if f.endswith(".asm")]

    for filename in asm_files:
        if path.isfile(filename + ".test"):
            test_file(filename)
        else:
            print_warn(filename + ".test is missing")

main()
