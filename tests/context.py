# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# example
from source.example.hello_world import hello_world

# 1 easy
from source.leetcode.two_sum import two_sum as TwoSum

# 96 medium
from source.leetcode.unique_bst import unique_bst as UniqueBST
