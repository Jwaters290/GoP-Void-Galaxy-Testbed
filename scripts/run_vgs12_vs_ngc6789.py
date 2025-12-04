# scripts/run_vgs12_vs_ngc6789.py

from pathlib import Path
from gop_void_testbed.io_utils import load_void_galaxies_from_json
from gop_void_testbed.metrics import lcdm_heaviness, gop_heaviness, metallicity_deficit

# Very rough "field relation" for 12 + log(O/H) vs MB; you can replace with a proper fit.
def expected_O_H_from_MB(MB: float) -> float | None:
    if MB is None:
        return None
    # Example: 12 + log(O/H) = a + b * MB  (toy placeholder)
    a, b = 6.0, -0.05
    return a + b * MB


def main():
    data_path = Path(__file__).parents[1] / "gop_void_testbed" / "examples" / "vgs12_ngc6789.json"
    galaxies = load_void_galaxies_from_json(data_path)

    print("\n=== Void Galaxy Comparison: ΛCDM vs GoP (toy testbed) ===\n")

    for g in galaxies:
        print(f"Galaxy: {g.name}")
        print(f"  Notes: {g.notes}")
        print(f"  M_star = {g.M_star:.3e} Msun")

        # Metallicities
        O_H_exp = expected_O_H_from_MB(g.MB) if g.MB is not None else None
        dZ = metallicity_deficit(g.O_H, O_H_exp) if g.O_H is not None else None
        if dZ is not None:
            print(f"  12+log(O/H)_obs = {g.O_H:.2f}, expected ≈ {O_H_exp:.2f}, ΔZ = {dZ:.2f} dex")

        # Heaviness proxies
        h_lcdm = lcdm_heaviness(g)
        h_gop = gop_heaviness(g, env_entropy_proxy=1.0)  # tune later
        print(f"  Heaviness ΛCDM proxy: {h_lcdm}")
        print(f"  Heaviness GoP proxy  : {h_gop}")

        if h_lcdm is not None and h_gop is not None:
            ratio = h_gop / (h_lcdm + 1e-12)
            print(f"  GoP/ΛCDM heaviness ratio ≈ {ratio:.2f}")

        print("")

if __name__ == "__main__":
    main()
