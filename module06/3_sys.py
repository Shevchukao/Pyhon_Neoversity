import sys

for mod in sys.modules:
    print(f"{mod}:{sys.modules[mod]}")  # all modules frozen, built-in

print()
print(sys.modules["sys"]) # Path for search module math
print()
print(sys.path)  # Path for search module
print()
print(sys.version)  # version python
print()
print(sys.version_info)  # version info python
print()
print(sys.platform)  # work in win32 platform
print()
print(sys.argv)


sys.exit()  # stop workin program don't work other commands down
filename = (
    "C:\\windows\\system32\\drivers\\etc\\hosts"
    if sys.platform == "win32"
    else "etc/hosts"
)
