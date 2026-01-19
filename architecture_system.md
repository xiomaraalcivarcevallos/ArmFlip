\# Data Architecture Flowchart | Project ArmFlip



This diagram illustrates the logical path of information from the initial design parameters to the physical execution of the 7th-axis system.



\### \[ DATA ARCHITECTURE FLOW ]



\[ 1. DESIGN LAYER ]

&nbsp;      |

&nbsp;      v

+-----------------------------+      +---------------------------+

|  Rhino + Grasshopper Logic  | ---> |  Geometry \& Path Targets  |

+-----------------------------+      +---------------------------+

&nbsp;                                            |

\[ 2. COMPUTATIONAL LAYER ]                   |

&nbsp;                                            v

&nbsp;                            +-------------------------------+

&nbsp;                            |  GHPython Kinematic Solver    |

&nbsp;                            |  (Axis Decomposition Logic)   |

&nbsp;                            +-------------------------------+

&nbsp;                                    /               \\

&nbsp;               \[Stream A: Robot Data]               \[Stream B: Gantry Data]

&nbsp;                         |                                    |

\[ 3. MIDDLEWARE LAYER ]   v                                    v

&nbsp;               +--------------------+               +-----------------------+

&nbsp;               | TCP/IP Socket Msg  |               | Serial / USB Command  |

&nbsp;               +--------------------+               +-----------------------+

&nbsp;                         |                                    |

\[ 4. HARDWARE LAYER ]     v                                    v

&nbsp;               +--------------------+               +-----------------------+

&nbsp;               |  UR3e Controller   | <-----------> | Arduino + Motor Driver|

&nbsp;               +--------------------+   (I/O Sync)  +-----------------------+

&nbsp;                         |                                    |

&nbsp;                         \\\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/

&nbsp;                                          \\/

&nbsp;                                 \[ COORDINATED MOTION ]

