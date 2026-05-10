import numpy as np
from scipy.ndimage import uniform_filter1d

# --------------------------------------------------
# Parameters
# --------------------------------------------------
N = 256

omega_list = [
    0.01 * np.pi,
    0.05 * np.pi,
    0.15 * np.pi,
    0.30 * np.pi
]

# --------------------------------------------------
# Known sequence
# --------------------------------------------------
np.random.seed(0)

s = np.random.choice([-1, 1], size=N).astype(complex)

# --------------------------------------------------
# Main loop
# --------------------------------------------------
for omega in omega_list:

    n = np.arange(N)

    # ----------------------------------------------
    # Doppler phase rotation
    # ----------------------------------------------
    r = s * np.exp(1j * omega * n)

    # ----------------------------------------------
    # Correlation accumulation
    # ----------------------------------------------
    corr_mag = []

    for L in range(1, N + 1):

        c = np.sum(r[:L] * np.conj(s[:L]))

        corr_mag.append(np.abs(c))

    corr_mag = np.array(corr_mag)

    # ----------------------------------------------
    # Normalize
    # ----------------------------------------------
    corr_mag_norm = corr_mag / np.max(corr_mag)

    # ----------------------------------------------
    # Incremental gain
    # ----------------------------------------------
    incremental_gain = np.diff(corr_mag_norm)

    # ----------------------------------------------
    # Smooth incremental gain
    # ----------------------------------------------
    incremental_gain_smooth = uniform_filter1d(
        incremental_gain,
        size=5
    )

    # ----------------------------------------------
    # First negative crossing
    # ----------------------------------------------
    zero_cross_idx = None

    for i in range(len(incremental_gain_smooth)):

        if incremental_gain_smooth[i] < 0:

            zero_cross_idx = i + 1
            break

    # fallback
    if zero_cross_idx is None:
        zero_cross_idx = N

    # ----------------------------------------------
    # Theoretical coherence boundary
    # ----------------------------------------------
    theory_boundary = int(np.pi / omega)
