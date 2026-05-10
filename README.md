# doppler-coherence-analysis
OFDM Doppler Coherence analysis and Visualization

## 1. Project overview

This project studies how Doppler-induced phase rotation affects coherent accumulation behavior in wireless receivers.

In many synchronization, detection, and channel-estimation algorithms, receiver performance depends on accumulating correlation energy over time. Under ideal static conditions, longer accumulation generally improves detection strength. However, in the presence of Doppler, phase rotation gradually reduces coherence, causing accumulation gain to saturate and eventually become destructive.

This repository investigates:

* correlation magnitude evolution versus accumulation length,
* incremental gain behavior during coherent accumulation,
* constructive and destructive accumulation regions,
* coherence-support width under Doppler,
* and the relationship between Doppler frequency and effective accumulation limits.

The work combines:

* simulation,
* signal-processing interpretation,
* and geometric/coherence-based intuition
  to study adaptive accumulation behavior in OFDM-style wireless systems.

The generated figures demonstrate how coherence support shrinks with increasing Doppler and how local incremental-gain analysis can reveal physically meaningful accumulation boundaries.

Potential applications include:

* adaptive receiver integration control,
* synchronization/search-window optimization,
* Doppler-aware accumulation strategies,
* pilot combining,
* and intelligent PHY adaptation frameworks.


2. Key idea

Constructive/destructive accumulation under Doppler.

3. Figures



4. How to run

Simple commands.

5. Future work

AWGN, multipath, adaptive stopping, AI estimation.
