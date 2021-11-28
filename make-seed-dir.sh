#!/usr/bin/env bash
set -ex

mkdir "$1"
cp s.py "$1"
cp grid.py "$1"
cp util.py "$1"
cp in "$1"
cp traversals.py "$1"
cp Makefile "$1"
