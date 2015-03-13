#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Interaction with existing list & performing access functions."""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[2] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])

print BALLETS
