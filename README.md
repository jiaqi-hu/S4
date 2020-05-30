S4: Stanford Stratified Structure Solver (http://fan.group.stanford.edu/S4/)

A program for computing electromagnetic fields in periodic, layered
structures, developed by Victor Liu (victorliu@alumni.stanford.edu) of the
Fan group in the Stanford Electrical Engineering Department.

See the S4 manual, in doc/index.html, for a complete
description of the package and its user interface, as well as
installation instructions, the license and copyright, contact
addresses, and other important information.

---

Compiling instructions for Lua interface

Prerequisites:
 - Lua 5.2.x (Windows, Linux, macOS)
 - OpenBLAS (Windows, Linux, [disabling multi-threading](https://github.com/xianyi/OpenBLAS/wiki/faq#multi-threaded) recommended)
 - MinGW-w64 toolchain from MSYS2 for Windows

Command to start compiling:

    make

Executable binary file location:

    build/S4 or build/S4.exe
