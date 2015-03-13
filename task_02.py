#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Interaction with existing list & performing access functions."""

from data import BALLETS

BALLETS = BALLETS

del BALLETS[11]

BALLETS[2] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])

print BALLETS
