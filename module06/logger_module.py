from colorama import Fore, Style, init

init(autoreset=True)


# BAD
# def debug(message):
#     return f"{Fore.BLUE}DEBUG: {message}{Style.RESET_ALL}"


# def info(message):
#     return f"{Fore.GREEN}INFO: {message}{Style.RESET_ALL}"


def log_message(lvl, message):
    lvl = lvl.upper()
    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }
    if lvl in COLORS.keys():
        return f"{COLORS[lvl]}{lvl}: {message}{Style.RESET_ALL}"
    else:
        return f"{Fore.WHITE}{lvl}: {message}{Style.RESET_ALL}"


def debug(message):
    return log_message("DEBUG", message)


def info(message):
    return log_message("INFO", message)


def warning(message):
    return log_message("WARNING", message)


def error(message):
    return log_message("ERROR", message)


def critical(message):
    return log_message("CRITICAL", message)


if __name__ == "__main__":

    print(debug("Problem with cable"))
    print(info("Problem with sysname"))
    print(critical("Port Gigabit1/1 is down"))
    print(error("Problem with SFP module"))
    print(warning("Port Gigabit1/1 is up"))
    print(dir())
