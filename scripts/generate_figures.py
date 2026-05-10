import numpy as np
import matplotlib.pyplot as plt
from utils import corr_mag_norm, zero_cross_idx, theory_boundary, omega, N, incremental_gain, incremental_gain_smooth
from utils import *

for omega in omega_list:
    # ==================================================
    # FIGURE A
    # Normalized correlation accumulation
    # ==================================================
    plt.figure(figsize=(10, 5))

    plt.plot(
        np.arange(1, N + 1),
        corr_mag_norm,
        linewidth=2
    )

    # Constructive region
    plt.axvspan(
        1,
        zero_cross_idx,
        alpha=0.15,
        label='Constructive Region'
    )

    # Destructive region
    plt.axvspan(
        zero_cross_idx,
        N,
        alpha=0.08,
        label='Destructive Region'
    )

    # Estimated boundary
    plt.axvline(
        zero_cross_idx,
        linestyle='--',
        linewidth=2,
        label='Observed Boundary'
    )

    # Theoretical boundary
    plt.axvline(
        theory_boundary,
        linestyle=':',
        linewidth=2,
        label='Theoretical π/ω Boundary'
    )

    plt.xlabel('Accumulation Length L')
    plt.ylabel('Normalized Correlation')

    plt.title(
        f'Figure A: Correlation Accumulation\n'
        f'ω = {omega / np.pi:.2f}π'
    )

    plt.grid(True)
    plt.legend()

    plt.savefig(
        f'FigureA_corr_omega_{omega / np.pi:.2f}pi.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()

    # ==================================================
    # FIGURE B
    # Incremental gain only
    # ==================================================
    plt.figure(figsize=(10, 5))

    plt.plot(
        np.arange(2, N + 1),
        incremental_gain,
        alpha=0.4,
        label='Raw Incremental Gain'
    )

    plt.plot(
        np.arange(2, N + 1),
        incremental_gain_smooth,
        linewidth=2,
        label='Smoothed Incremental Gain'
    )

    # Zero line
    plt.axhline(
        0,
        linestyle='--',
        linewidth=1
    )

    # Boundary
    plt.axvline(
        zero_cross_idx,
        linestyle='--',
        linewidth=2,
        label='Observed Boundary'
    )

    # Theoretical boundary
    plt.axvline(
        theory_boundary,
        linestyle=':',
        linewidth=2,
        label='Theoretical π/ω Boundary'
    )

    plt.xlabel('Accumulation Length L')
    plt.ylabel('Incremental Gain')

    plt.title(
        f'Figure B: Incremental Gain Evolution\n'
        f'ω = {omega / np.pi:.2f}π'
    )

    plt.grid(True)
    plt.legend()

    plt.savefig(
        f'FigureB_incremental_omega_{omega / np.pi:.2f}pi.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()

    # ==================================================
    # FIGURE C
    # Unified annotated figure
    # ==================================================
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Correlation magnitude
    ax1.plot(
        np.arange(1, N + 1),
        corr_mag_norm,
        linewidth=2,
        label='Normalized Correlation'
    )

    ax1.set_xlabel('Accumulation Length L')
    ax1.set_ylabel('Normalized Correlation')

    # Constructive region
    ax1.axvspan(
        1,
        zero_cross_idx,
        alpha=0.15,
        label='Constructive Region'
    )

    # Destructive region
    ax1.axvspan(
        zero_cross_idx,
        N,
        alpha=0.08,
        label='Destructive Region'
    )

    # Observed boundary
    ax1.axvline(
        zero_cross_idx,
        linestyle='--',
        linewidth=2,
        label='Observed Boundary'
    )

    # Theoretical boundary
    ax1.axvline(
        theory_boundary,
        linestyle=':',
        linewidth=2,
        label='Theoretical π/ω Boundary'
    )

    # ----------------------------------------------
    # Secondary axis
    # ----------------------------------------------
    ax2 = ax1.twinx()

    ax2.plot(
        np.arange(2, N + 1),
        incremental_gain_smooth,
        linewidth=2,
        alpha=0.8,
        label='Smoothed Incremental Gain'
    )

    ax2.axhline(
        0,
        linestyle='--',
        linewidth=1
    )

    ax2.set_ylabel('Incremental Gain')

    # ----------------------------------------------
    # Title
    # ----------------------------------------------
    plt.title(
        f'Figure C: Unified Doppler Accumulation Analysis\n'
        f'ω = {omega / np.pi:.2f}π'
    )

    # ----------------------------------------------
    # Combined legend
    # ----------------------------------------------
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc='best'
    )

    plt.grid(True)

    plt.savefig(
        f'FigureC_unified_omega_{omega / np.pi:.2f}pi.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()

print("All figures generated successfully.")