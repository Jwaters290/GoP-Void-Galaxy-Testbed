# gop_void_testbed/data_models.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class VoidGalaxy:
    name: str
    M_star: float               # stellar mass in Msun
    M_HI: Optional[float]       # HI mass in Msun (if available)
    MB: Optional[float]         # absolute B magnitude
    O_H: Optional[float]        # 12 + log(O/H)
    N_O: Optional[float]        # log(N/O)
    r_over_Rv: Optional[float]  # host void-centric radius, r/R_void (if known/estimated)
    isolation_flag: bool        # True if extremely isolated / Local Void, etc.
    notes: str = ""             # free-form notes

    def gas_fraction(self) -> Optional[float]:
        if self.M_HI is None or self.M_star is None:
            return None
        return self.M_HI / (self.M_HI + self.M_star)
