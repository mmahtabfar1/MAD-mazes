from distutils.core import setup, Extension

with open("README.md", "r") as file:
    long_description = file.read()

ext = Extension("ext", sources=["./ext/ext.c", "./ext/PQ.c", "./ext/Stack.c"],
                include_dirs=["./ext"])

setup(
    name="MAD-mazes",
    author="Mahan Mahtabfar, Derek Musial, Amer Khalifa",
    description="Program to visualize and apply pathfinding algorithms",
    long_description=long_description,
    version="1.0",
    ext_modules=[ext],
)
