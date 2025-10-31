# C Skeleton

This workspace now includes a minimal C project skeleton.

Files:
- `main.c` - simple Hello World program.
- `Makefile` - build and clean targets (`make` / `make clean`).

To build and run on Windows with MinGW or WSL installed:

- Using MinGW (from PowerShell):
  gcc -o main main.c
  .\main.exe

- Using WSL or a Unix-like shell:
  make
  ./main

