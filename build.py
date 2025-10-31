#!/usr/bin/env python3
"""
Simple build script for static sites on Render.
Copies repository files into a `publish/` folder excluding common dev dirs.
Usage: python build.py
After running, point Render's Publish Directory to `publish` and set Build Command to `python build.py`.
"""
import os
import shutil

IGNORES = {'.git', '.venv', 'venv', 'node_modules', 'publish', '__pycache__', '.pytest_cache'}


def should_ignore(name):
    return name in IGNORES


def copy_project(src='.', dst='publish'):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    def _ignore(dir, entries):
        return [e for e in entries if should_ignore(e)]

    shutil.copytree(src, dst, ignore=_ignore)

    # Double-check and remove any ignored dirs that slipped through
    for root, dirs, files in os.walk(dst):
        for d in list(dirs):
            if should_ignore(d):
                shutil.rmtree(os.path.join(root, d))

    print(f'Published static files to: {dst}')


if __name__ == '__main__':
    copy_project()
