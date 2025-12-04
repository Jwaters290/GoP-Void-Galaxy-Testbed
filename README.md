# Void-Center Galaxies and the Gravity of Probability Framework: Pre-DESI Consistency with VGS 12 and NGC 6789.
This repository accompanies the Figshare paper “Void-Center Galaxies and the Gravity of Probability Framework: Pre-DESI Consistency with VGS 12 and NGC 6789.”
It provides a reproducible Python testbed for comparing standard ΛCDM expectations with Gravity of Probability (GoP) “core-four aware” predictions in isolated void galaxies. The code implements the unified GoP parameter set, the decoherence kernel, ΛCDM baselines, and tools for analyzing metallicity deficits, N/O enrichment, and dynamical heaviness.
The corresponding paper is available at:
https://figshare.com/articles/figure/Void-Center_Galaxies_and_the_Gravity_of_Probability_Framework_Pre-DESI_Consistency_with_VGS_12_and_NGC_6789/30701561

---

# GoP-Void-Galaxy-Testbed
A python demonsstration comparing ΛCDM void expectations vs GoP core-four standards applied to actual void galaxies (like VGS 12, NGC 6789 now, DESI void galaxies later).

```
GoP-Void-Galaxy-Testbed/
├─ README.md
├─ pyproject.toml          # or setup.cfg / setup.py if you prefer
├─ gop_void_testbed/
│  ├─ __init__.py
│  ├─ config_core_four.py
│  ├─ data_models.py
│  ├─ gop_core.py
│  ├─ lcdm_void.py
│  ├─ metrics.py
│  ├─ io_utils.py
│  └─ examples/
│     ├─ vgs12_ngc6789.json
│     └─ vgs12_ngc6789.csv
├─ scripts/
│  ├─ run_vgs12_vs_ngc6789.py
│  └─ plot_void_galaxy_metrics.py
└─ notebooks/
   ├─ 01_vgs12_gop_vs_lcdm.ipynb        # optional, you can create in Jupyter later
   └─ 02_mock_void_stack_demo.ipynb     # placeholder for DESI/EUCLID era
```
---

## Philosophy:

Small, composable modules (GoP kernel, ΛCDM toy void model, metrics).

Data-agnostic: today we use VGS 12 & NGC 6789; later you just drop in DESI VAC slices.

“Core-four aware”: one central source of truth for 𝜅𝐴, 𝐸0, 𝑓ent, 𝐴CP

---

# κA - curvature conversion strength Parameter.

κA was fixed by requiring simultaneous agreement with:

1. SPARC galaxy rotation curves
 – must produce flat rotation curves with the same parameter set across 175 galaxies.

2. Bullet Cluster and lensing clusters
 – must reproduce mass offsets using probabilistic curvature without dark matter.

3. Cosmic void warm-core amplitude
 – requires curvature contribution small but nonzero in void centers.

4. CMB low-ℓ suppression amplitude
 – must not overproduce large-scale gravitational potentials.

The cross-fit pointed to a very small, stable constant.

Final Value
𝜅𝐴=1.5×10^−15*s^−1*erg^−1

This is the “universal curvature efficiency” of decoherence.

---

# E₀ — Decoherence Energy Scale Parameter.
Description
𝐸_0 is the characteristic energy scale of the decoherence kernel:

Γ(𝐸)=𝜅𝐴*𝐸𝑒^−𝐸/𝐸0.

It controls where decoherence is maximally gravitationally active:

 - For 𝐸≪𝐸_0: increasing energy increases decoherence.
 - For E≫E_0: the effect shuts off exponentially.

The peak gravitational contribution occurs near E=E_0.

Derivation

𝐸_0 is fixed by requiring consistent predictions for:

1. Small dwarf galaxies (SPARC low-mass set)
 – need strong decoherence effect at low energies.

2. Larger galaxies and clusters
 – decoherence must naturally suppress to avoid over-curving high-mass systems.

3. CMB anisotropy amplitude
 – energy scale must align with the decoherence suppressing low-ℓ modes.

4. Path-integral field theory quantization
 – the scalar field 𝜌Ψ acquires a natural scale near 10^12 erg from renormalization constraints.

Final Value
𝐸_0=1.0×10^12erg

This is the universal decoherence energy resonance scale, matching dwarfs, clusters, CMB, and BAO.

---

# fₑₙₜ — Quantum Entanglement Fraction Parameter.
Description:
fₑₙₜ measures the fraction of energy density stored in long-range entanglement correlations that survive coarse-graining and contribute to spacetime curvature.

It weights how strongly nonlocal quantum correlations enhance or suppress probabilistic curvature.

Derivation:

fₑₙₜ was introduced during the quantum extension of GoP in the path-integral formalism. It is constrained by:

1. CMB low-ℓ suppression
 – requires ≈10–25% entanglement contribution.

2. Galaxy rotation curve stability
 – too large → overshoots dwarfs; too small → underpredicts mid-mass systems.

3. Cluster lensing
 – entanglement contribution must enhance curvature without requiring dark matter halos.

4. RG flow from the scalar field 𝜌Ψ
 – yields an effective entanglement residue ~0.2 after coarse-graining.

Final Value
𝑓_ent=0.20

Meaning: 20% of decoherence energy contributes nonlocally and must be included in the curvature source.

---

# A_CP — CP-Violation Curvature Asymmetry Parameter.
Description:
𝐴_CP encodes a small asymmetry in the decoherence kernel caused by matter–antimatter CP violation, emerging naturally in your quantized Lagrangian:

𝐿_int⊃𝐴_CP*𝜌Ψ𝜓ˉ𝛾5𝜓.

It functions as a bias term that slightly favors baryonic decoherence contributions over antibaryonic ones.

Derivation:
𝐴_CP

is fixed using:
1. LHCb measurement of Λ𝑏0 CP violation
 – the 5.2σ result gives:

𝐴_CP≈0.0245.

2. CMB odd-parity suppression
 – requires a nonzero asymmetry consistent with ~2–3%.

3. Asymmetric decoherence field behavior in the early universe
 – especially during baryogenesis and recombination.

4. Stability of galaxy fits
 – the asymmetry must be small enough not to distort rotation curve universality.

Final Value
𝐴_CP=0.0245

This places the curvature asymmetry exactly in the range inferred from experiment.


---

# GoP-Void-Galaxy-Testbed

A lightweight Python testbed for comparing:

- ΛCDM expectations for void galaxies, and
- Gravity of Probability (GoP) "core-four" predictions

against observed properties of galaxies in underdense environments
(e.g. VGS 12, NGC 6789, and future DESI/EUCLID void galaxies).

## Features

- Implements the GoP decoherence kernel Γ(E) with fixed "core-four" parameters.
- Simple ΛCDM toy expectations for void-galaxy dynamics and environment.
- Common metrics for "anomaly strength" (metallicity deficit, N/O excess,
  dynamical heaviness, isolation, etc.).
- Example dataset: VGS 12 and NGC 6789 pre-DESI.

## Install

```bash
pip install -e .
```


----

## Quickstart

```bash
python scripts/run_vgs12_vs_ngc6789.py
python scripts/plot_void_galaxy_metrics.py
```


