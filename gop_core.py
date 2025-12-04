# gop_void_testbed/gop_core.py

import numpy as np
from .config_core_four import CORE_FOUR

def gamma_E(E, kappaA=None, E0=None):
    """
    GoP decoherence kernel Γ(E) = κA * E * exp(-E / E0)

    Parameters
    ----------
    E : float or array-like
        Characteristic energy scale in erg.
    kappaA : float, optional
        Prefactor κA. Defaults to CORE_FOUR.kappaA.
    E0 : float, optional
        Decoherence scale E0. Defaults to CORE_FOUR.E0.
    """
    if kappaA is None:
        kappaA = CORE_FOUR.kappaA
    if E0 is None:
        E0 = CORE_FOUR.E0

    E = np.asarray(E, dtype=float)
    return kappaA * E * np.exp(-E / E0)


def zeta_from_gamma(gamma_eff, gamma_star=1.0):
    """
    Simple saturating map from Γ_eff / Γ_* to a dimensionless curvature weight ζ.

        ζ(x) = x / (1 + x),  with x = Γ_eff / Γ_*

    This is a placeholder / proxy for the full probabilistic curvature response.
    """
    x = np.asarray(gamma_eff, dtype=float) / gamma_star
    return x / (1.0 + x)


def effective_void_potential_boost(env_entropy_proxy, gamma_star=1.0):
    """
    Map an 'environment entropy / decoherence proxy' to an effective potential boost.

    Parameters
    ----------
    env_entropy_proxy : float
        Some toy proxy for decoherence activity in the void environment; could be
        related to SFR, gas turbulence, etc. For now, we treat it as dimensionless.
    gamma_star : float
        Reference decoherence rate.

    Returns
    -------
    float
        Dimensionless potential boost factor Φ_GoP / Φ_LCDM.
    """
    gamma_eff = gamma_E(env_entropy_proxy)
    zeta = zeta_from_gamma(gamma_eff, gamma_star=gamma_star)
    # For the testbed: 1 + ζ acts as a multiplicative boost on the effective potential
    return 1.0 + zeta
