# A bound for synchronous parallel carries in binary multiplication

An **AI-assisted mathematical research note** addressing the **first inequality of Question 3** in Masamichi Iizumi's 2026 paper, *Binary convolution height: Structural invariants of integer factorisations* ([DOI](https://doi.org/10.1080/27684830.2026.2727395)).

**Research conception, framing and coordination:** Joan Abad.  
**Mathematical derivation, literature screening, computation and drafting:** substantial AI assistance, disclosed openly.  
**Original mathematical context and extremal examples:** Dr. Masamichi Iizumi (2026), whose work is central to this note.

This is **not a peer-reviewed article**. The note offers a complete short proof and reproducible finite checks; the review of earlier literature was selective, so **global originality is not claimed or certified**.

## Result

For positive integers `a,b`, let `L_par(a,b)` count the rounds needed to normalize their binary digit convolution when all available carry pairs at every column are processed **simultaneously**, using only digits from the previous round. We prove

$$
L_{\mathrm{par}}(a,b)\leq \lfloor\log_2a\rfloor+\lfloor\log_2b\rfloor.
$$

The argument also establishes

$$
L_{\mathrm{par}}(a,b)\leq\max\{0,\operatorname{bitlength}(ab)-2\}.
$$

The original bound is sharp, as shown by **Iizumi's previously published extremal family**. See [NOTE.md](NOTE.md) for definitions, proof, examples, limits, attribution and references.

## Reproduce the finite controls

```bash
python3 verify.py
```

Requires only Python 3 standard library. The script checks 262,144 ordered factor pairs (`1 <= a,b <= 512`), 15,625 nonnegative digit vectors, weighted-value preservation, two illustrative equality cases and a negative control. Expected output:

```text
B1_SYNTHETIC_INDEPENDENT_CONTROL_PASS convolution_pairs=262144 general_vectors=15625 bound_equalities=12 max_rounds=14 negative_control=PASS worked_traces=PASS
```

**Finite computation is not a proof**: the universal argument appears in the note. AI-only mathematical review is also **not** independent human peer review.

## Invitation to mathematical scrutiny

We welcome reproducible counterexamples, corrections to the proof, and **precise references to earlier equivalent theorems**, particularly concerning redundant binary digit normalization and batched chip-firing. Please [open an issue](../../issues) and identify the relevant hypotheses, round definition, and theorem or calculation. Verified corrections and priority claims will be incorporated with attribution.

## Scope and provenance

- B1 only: the first inequality of Iizumi's Question 3. We do **not** claim to resolve the separate height/popcount question.
- This repository is a standalone mathematical note, **not** the private SpectralCode system and not evidence of improved SpectralCode performance.
- The mathematical framing and research coordination are attributed to Joan Abad, without claiming exclusive human discovery of the proof.
- The question, update model, and sharpness-family precedent are credited to Dr. Iizumi; other related work is cited in the note.

No license is granted in this initial release. Attribution and rights can be revisited explicitly; GitHub visibility alone does not assign an open-source license.
