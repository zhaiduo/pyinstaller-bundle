#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def main():
    subprocess.call([resource_path(os.path.join('bundle-category', 'bundle.exe')), "parameters"])

if __name__ == "__main__":
    main()

