# 🛠️ Installation & Configuration Guide | AIRFLIP

This document provides the technical instructions required to set up the software and hardware environment for the **AIRFLIP Rotary Gantry System**, developed for the **MRAC Workshop 2.1 (2026)**.

---

## 1. Software Setup

### 🐍 Python Environment
The system is built on **Python 3.9+**. We recommend using a virtual environment (venv or conda) to manage dependencies and maintain a clean workspace.

**Installation Steps:**
```bash
# Clone the repository
git clone [https://github.com/xiomaraalcivarcevallos/MRAC-IAAC-ArmFlip.git](https://github.com/xiomaraalcivarcevallos/MRAC-IAAC-ArmFlip.git)
cd MRAC-IAAC-ArmFlip

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### C++ Hardware Controller
The low-level controller for high-speed synchronization is written in C++. It requires CMake 3.10+ and a C++17 compatible compiler.

Build Instructions:
```bash

mkdir build && cd build
cmake ..
make
```

## 2. Mandatory Configuration Files
requirements.txt
Create this file in the root directory to ensure all libraries match our development version:

```plaintext
# AIRFLIP System Dependencies
pyserial>=3.5
numpy>=1.24.0
ur-rtde>=1.5.5
pyyaml>=6.0
```

Use this configuration to handle threading and real-time control:

```CMake

cmake_minimum_required(VERSION 3.10)
project(AirFlipHardware)

# Set C++ Standard to 17 for modern robotics libraries
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Define the executable from your source
add_executable(hardware_controller hardware_controller.cc)

# Link threading libraries essential for real-time synchronization
find_package(Threads REQUIRED)
target_link_libraries(hardware_controller PRIVATE Threads::Threads)
```

