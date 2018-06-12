from colorama import init, Fore, Style
from tabulate import tabulate

# include logger functionality

# Make class and define dbg as static value

dbg = 1


def psetup():
    init()


def testdebug():
    return dbg


def pheader(header=''):
    if dbg:
        print(Fore.LIGHTBLUE_EX + header + Style.RESET_ALL)

def psuccess(successmsg=''):
    print(Fore.GREEN + successmsg + Style.RESET_ALL)

def pdebug(debug=''):
    if dbg:
        print(debug)


def pwarning(warning=''):
    print(Fore.YELLOW + warning + Style.RESET_ALL)


def perror(error='', cond=0):
    error = Fore.RED + error + Style.RESET_ALL
    assert cond, error


def ptable(header, body):
    assert isinstance(header, list) and isinstance(body, list)

    for ind in range(0,len(header)):
        header[ind] = Fore.GREEN + header[ind]

        if ind == len(header)-1:
            header[ind] += Style.RESET_ALL

    print(tabulate(body, headers=header))










