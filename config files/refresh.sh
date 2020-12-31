#!/bin/bash
echo "Actualizando archivos..."

cp ~/.bashrc bashrc
pacman -Qet > pakagesPacman.txt
cp ~/.config/qtile/config.py QT-config.py

echo "hecho"

