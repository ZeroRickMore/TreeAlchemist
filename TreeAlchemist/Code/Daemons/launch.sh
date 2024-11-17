#!/bin/bash

# Open the first terminal and run the first Python script
gnome-terminal -- bash -c "python3 ./tree_alchemized_log_monitord.py; exec bash"

# Open the second terminal and run the second Python script
gnome-terminal -- bash -c "python3 ./Athanor.py; exec bash"