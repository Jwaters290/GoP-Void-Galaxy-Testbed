# gop_void_testbed/lcdm_void.py

import numpy as np

def lcdm_void_density_contrast(r_over_Rv, delta_c=-0.8):
    """
    Simple toy ΛCDM void density contrast profile δ(r)/ρ̄.

    Parameters
    ----------
    r_over_Rv : float or array-like
        Radius normalized by void effective radius Rv.
    delta_c : float
        Central density contrast (e.g., -0.8 for a deep void).

    Returns
    -------
    delta : float or array-like
        Density contrast δ(r) = ρ(r)/ρ̄ - 1
    """
    x = np.asarray(r_over_Rv, dtype=float)
    # Very simple smooth profile: central underdensity that recovers to 0 at x=1
    # δ(r) = δ_c * (1 - x^2), truncated at 0
    delta = delta_c * np.clip(1.0 - x**2, 0.0, 1.0)
    return delta


def expected_void_galaxy_potential(r_over_Rv, delta_c=-0.8):
    """
    Toy estimate of normalized potential depth for a galaxy at radius r in a ΛCDM void.

    We just integrate the toy δ(r) profile in a crude way, then rescale to [0, 1].

    Returns
    -------
    float or array-like
        Dimensionless potential depth proxy Φ_LCDM(r).
    """
    delta = lcdm_void_density_contrast(r_over_Rv, delta_c=delta_c)
    # crude mapping: more negative δ → shallower potential
    # we invert sign and renormalize.
    phi = -delta  # deeper potential when δ is less negative
    # renormalize between 0 and 1
    phi_min, phi_max = 0.0, 1.0
    return np.clip((phi - phi_min) / (phi_max - phi_min + 1e-12), 0.0, 1.0)
