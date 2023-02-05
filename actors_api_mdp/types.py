"""
This module contains the main type definitions.

In particular:
- State is the type of state;
...
"""
from typing import Any, Dict, Hashable, Tuple

State = Hashable
Action = Any
Reward = float
Prob = float
TransitionFunction = Dict[State, Dict[Action, State]]
TransitionFunctionReward = Dict[State, Dict[Action, Tuple[Dict[State, Prob], Reward]]]
