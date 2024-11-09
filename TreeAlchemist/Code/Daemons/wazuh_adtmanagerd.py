'''
Script to handle the defense launch, based off the current ADT state.

It uses the same State and Tree classes used in TreeAlchemist,
and maps each agent to a list of states based on the ADT.
Realistically, it is a dictionary from {ADT_id (int) : state (list[int])

This manager gets the alerts raised from syslog

The folder ADT_generation_files contains a set of text files that help recreate the tree and nodes very simply
'''


