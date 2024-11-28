#!/bin/bash

# Open the first terminal and run the first Python script
gnome-terminal --geometry=100x24 -- bash -c "python3 ./Observer.py; exec bash"

# Open the second terminal and run the second Python script
gnome-terminal --geometry=100x24 -- bash -c "python3 ./Athanor.py; exec bash"
