# gop_void_testbed/metrics.py

import numpy as np
from .lcdm_void import expected_void_galaxy_potential
from .gop_core import effective_void_potential_boost

def metallicity_deficit(O_H_obs, O_H_expected):
    """
    ΔZ = (O/H)_obs - (O/H)_expected  in dex.
    Negative = 'too metal-poor' relative to field relation.
    """
    if O_H_obs is None or O_H_expected is None:
        return None
    return O_H_obs - O_H_expected


def heaviness_proxy_from_potential(phi_effective):
    """
    Simple mapping: more potential depth => larger 'heaviness' factor.
    """
    return 1.0 + phi_effective


def lcdm_heaviness(galaxy):
    """
    Toy ΛCDM heaviness proxy based purely on void-centric radius.

    For r/Rv -> 0: galaxy in deepest void center, shallower Φ under ΛCDM → modest heaviness.
    """
    if galaxy.r_over_Rv is None:
        return None
    phi_lcdm = expected_void_galaxy_potential(galaxy.r_over_Rv)
    return heaviness_proxy_from_potential(phi_lcdm)


def gop_heaviness(galaxy, env_entropy_proxy=1.0):
    """
    GoP heaviness proxy using effective decoherence-driven potential boost.

    env_entropy_proxy can later be tied to SFR, turbulence, or something more physical.
    """
    if galaxy.r_over_Rv is None:
        return None
    # Start from the same toy ΛCDM potential as baseline:
    phi_lcdm = expected_void_galaxy_potential(galaxy.r_over_Rv)
    boost = effective_void_potential_boost(env_entropy_proxy)
    phi_gop = phi_lcdm * boost
    return heaviness_proxy_from_potential(phi_gop)
