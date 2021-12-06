from dive import dive
from sonar_sweep import sonar_sweep
from binary_diagnostic import binary_diagnostic
from giant_squid import giant_squid

if __name__ == "__main__":

    print("ADVENT OF CODE 2021\n")

    print("- Day 1 -")
    sonar_sweep.do_challenges()

    print("\n- Day 2 -")
    dive.do_challenges()

    print("\n- Day 3 -")
    binary_diagnostic.do_challenges()

    print("\n- Day 4 -")
    giant_squid.do_challenges()
