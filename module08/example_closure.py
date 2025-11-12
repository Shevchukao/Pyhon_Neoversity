from datetime import datetime


def init_log(filename: str, reset=True):

    def read_log():
        with open(filename, "r") as f:
            return f.readlines()

    def write_log(message: str):
        with open(filename, "a") as a:
            return a.write(f"{datetime.now()} : {message}\n")

    if reset:
        f = open(filename, "w")  # rewrite file
        f.close()  # close file

    return read_log, write_log


if __name__ == "__main__":
    read, write = init_log("log.txt", reset=True)  # if False rewrite
    write("some action")
    write("another action")
    write("one more action")
    for line in read():
        print(line.rsplit())
