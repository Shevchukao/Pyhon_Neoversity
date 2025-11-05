import sys

for mod in sys.modules:
    print(f"{mod}:{sys.modules[mod]}")  # all modules frozen, built-in

print(sys.path)  # Path for search module
print(sys.version)  # version python
print(sys.version_info)  # version info python
print(sys.platform)  # work in win32 platform


sys.exit()  # stop workin program don't work other commands down
filename = (
    "C:\\windows\\system32\\drivers\\etc\\hosts"
    if sys.platform == "win32"
    else "etc/hosts"
)
