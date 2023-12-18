**_stress-ng Workload Simulator_**
# A stress/load simulator for UNIX environment

stress-ng is a tool for stressing and testing a computer system. It is designed to impose a configurable amount of CPU, memory, I/O, and other system-related stress on the hardware, helping users and administrators identify potential issues such as system instability, hardware faults, or inadequate cooling.

## Use Case
A sample script to simulate cpu workloads on your environment to stress test your system.
Workload1: SAPHANA (progressively increasing)
WorkLoad2: Stock Market (Workload heavy during trading hours)

## Install and Run
On Ubuntu/Debian-based Systems:
    ```
    sudo apt-get install stress-ng
    ```

After clone:
    ```
    cd stress-ng-workload-simulator
    python .\scriptname.py # assumes python is in your PATH
    ```