from distutils.core import setup, Extension

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="custom",
    author="Mahan Mahtabfar, Derek Musial, Amer Khalifa",
    description = "Program to visualize and apply pathfinding algorithms",
    long_description = long_description,
    version="1.0",
    ext_modules=[Extension("PQ", ["./ext/PQ.c"])],
)

