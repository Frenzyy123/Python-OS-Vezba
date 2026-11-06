import platform


print(f"{platform.python_version()}\n"
      f"{platform.machine()},"
      f"\n{platform.platform()}"
      f"\n"f"{platform.system()}")
if platform.python_version()[0] != '3':
    print("Ne koristite pravu verziju")
else:
    print("Koristite pravu verziju")