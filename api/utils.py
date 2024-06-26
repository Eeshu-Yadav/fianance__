from functools import partial

def ReExecuteLeg():
    print("Reexecuting legs")

def ReEnterLeg():
    print("Reentering legs")

def KeepLegRunning():
    print("Keeping legs running")

def execute_legs(legs):
    print(f"Executing legs: {legs}")

#def reexecute_at_opposite_leg_ltp(oppo_leg):
    #print(f"Reexecuting at opposite leg LTP: {oppo_leg}")

def reexecute_at_opposite_leg_ltp(legs):
    print(f"Reexecuting at opposite leg LTP: {legs}")

def sqoff_legs(legs):
    print(f"Squaring off legs: {legs}")

def Pyramiding():
    print(f"Pyramiding")

partial_execute_legs = partial(execute_legs, legs=[])
#partial_reexecute_opposite_leg = partial(reexecute_at_opposite_leg_ltp, oppo_leg=0)
partial_reexecute_opposite_leg = partial(reexecute_at_opposite_leg_ltp, legs=[])
partial_sqoff_legs = partial(sqoff_legs, legs=[])

ON_TP_FUNCTIONS = {
    'ReExecuteLeg': ReExecuteLeg,
    'ReEnterLeg': ReEnterLeg,
    'KeepLegRunning': KeepLegRunning,
    'partial_reexecute_opposite_leg': partial_reexecute_opposite_leg,
    'partial_sqoff_legs': partial_sqoff_legs,
    'partial_execute_legs': partial_execute_legs,
    'Pyramiding': Pyramiding,
}

ON_SL_FUNCTIONS = {
    'ReExecuteLeg': ReExecuteLeg,
    'ReEnterLeg': ReEnterLeg,
    'KeepLegRunning': KeepLegRunning,
    'partial_reexecute_opposite_leg': partial_reexecute_opposite_leg,
    'partial_sqoff_legs': partial_sqoff_legs,
    'partial_execute_legs': partial_execute_legs,
    'Pyramiding': Pyramiding,
}
