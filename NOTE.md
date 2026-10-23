# A short proof of a sharp parallel-carry bound for binary convolution

*An AI-assisted mathematical note on the first inequality of Iizumi's Question 3 (2026)*

**Research framing and coordination:** Joan Abad  
**Derivation and verification:** developed with substantial AI assistance, disclosed below.

## Statement and definitions

Masamichi Iizumi's article [1] introduces the parallel carry depth of a binary convolution. Let $a,b$ be positive integers with binary expansions $a=\sum_i a_i2^i$ and $b=\sum_i b_i2^i$, where $a_i,b_i\in\{0,1\}$. The initial pre-carry digit vector is

$$
d_j^{(0)}=\sum_{r+s=j}a_rb_s\quad(j\geq0).
$$

All digits are nonnegative integers; absent positions are zero. At every **synchronous full-batch** round,

$$
d_j^{(t+1)}=\left(d_j^{(t)}\bmod 2\right)
+\left\lfloor\frac{d_{j-1}^{(t)}}2\right\rfloor,
\qquad d_{-1}^{(t)}=0.
$$

Every right-hand side uses the **previous** configuration. Let $L_{\mathrm{par}}(a,b)$ be the least nonnegative round at which every digit lies in $\{0,1\}$.

**Theorem (first inequality of Iizumi's Question 3 [1]).** For all $a,b\geq1$,

$$
\boxed{L_{\mathrm{par}}(a,b)\leq
\lfloor\log_2a\rfloor+\lfloor\log_2b\rfloor.}
$$

The bound is sharp for infinitely many factor pairs, by the family **already given by Iizumi** in [1, Proposition 1].

## Proof

Set $N=ab$. The weighted value remains invariant in each round:

$$
\sum_{j\geq0}2^j d_j^{(t)}=N.
$$

Indeed, writing $q_j=\lfloor d_j^{(t)}/2\rfloor$, the local update subtracts $2q_j$ at position $j$ and adds $q_j$ at position $j+1$; the changes cancel in the weighted sum. All digits stay nonnegative.

The least significant initial digit satisfies $d_0^{(0)}=a_0b_0\in\{0,1\}$. An induction shows that after $t$ rounds, **all** positions $0\leq j\leq t$ are binary: settled positions emit no further carry, remain settled, and the next position becomes its former remainder modulo two.

Let $s=\operatorname{bitlength}(N)$, so $2^{s-1}\leq N<2^s$. By nonnegativity and conservation, at every time $d_j=0$ for $j\geq s$, while $d_{s-1}\leq1$: otherwise one digit alone would contribute at least $2^s>N$. Therefore, after $\max\{0,s-2\}$ rounds, the induction has settled every position below $s-1$, and the highest possible position was binary already. Thus

$$
\boxed{L_{\mathrm{par}}(a,b)\leq
\max\{0,\operatorname{bitlength}(ab)-2\}.}
$$

Finally, $ab<2^{\lfloor\log_2a\rfloor+\lfloor\log_2b\rfloor+2}$ implies the stated inequality. If either factor is $1$ (indeed, a power of two), the initial convolution is already binary and $L_{\mathrm{par}}=0$. $\square$

## Worked examples and sharpness

Vectors are listed **least significant position first**. Each arrow is one simultaneous full-batch round.

**Example A: $3\times3=9$.**

```text
(1,2,1)  ->  (1,0,2)  ->  (1,0,0,1)
```

The final digits represent binary `1001`. Exactly $L_{\mathrm{par}}=2$ rounds are needed, matching $\lfloor\log_23\rfloor+\lfloor\log_23\rfloor$.

**Example B: $3\times11=33$.**

```text
(1,2,1,1,1)  ->  (1,0,2,1,1)  ->  (1,0,0,2,1)
             ->  (1,0,0,0,2)  ->  (1,0,0,0,0,1)
```

The final digits represent binary `100001`. Exactly $L_{\mathrm{par}}=4$ rounds are needed, attaining both bounds. **This construction predates this note**: it is the $k=5$ instance of Iizumi's extremal family [1, Proposition 1], $a=3$, $b=(2^k+1)/3$ for odd $k\geq3$, with $L_{\mathrm{par}}=k-1$.

**Necessary hypothesis.** An arbitrary initial state $(2)$ has weighted value $N=2$ and becomes $(0,1)$ after one round. It violates the strengthened $\operatorname{bitlength}(N)-2$ bound because its least-significant initial digit is **not** binary. Our theorem concerns binary convolutions, for which this condition always holds.

**Scheduling matters.** The update processes $\lfloor d_j/2\rfloor$ carries per column. Rules permitting only one firing per active position per round can have different durations. Local equivalence to chip-firing does not automatically transfer parallel-depth bounds.

## Reproducible checks and limits

Run `python3 verify.py` to check 262,144 ordered pairs $1\leq a,b\leq512$, 15,625 six-column nonnegative vectors with digits in $\{0,1,2,3,4\}$, weighted value, examples and a negative control. Finite enumeration and an isolated AI mathematical critique found no errors within their stated scope. **Neither finite checks nor AI critique substitutes for the universal proof or constitutes human peer review.**

A bounded examination of prior literature did not identify an explicitly identical theorem with these precise initialization, update schedule and deterministic bound. **Global originality is not certified.** Carrying, redundant binary normalization and relationships to chip-firing have extensive antecedents [2–5].

This note addresses **only the first inequality of Question 3** in [1]. It does **not** settle the separate height/popcount question, introduce a new carry algorithm, or establish anything about private SpectralCode performance.

## Contributions, acknowledgments and invitation

**Joan Abad** identified the relevance of this mathematical question to the CarryDecoder/SpectralCode research, framed the investigation, established its scope and verification criteria, and coordinated its critical assessment.

The proof's derivation, computational checks, literature screening and drafting were developed with **substantial AI assistance**. No exclusive human derivation, external peer review, or established historical priority is claimed.

**Special acknowledgment to Dr. Masamichi Iizumi:** his 2026 article [1] provided the original question, the precise parallel-carry framework and the extremal family establishing sharpness. These are **his earlier contributions**. Other related work is credited in the references.

Mathematicians and other readers are invited to submit **specific corrections, reproducible counterexamples, or precise citations to earlier equivalent theorems** via [repository issues](../../issues). Please specify the notion of a parallel round and the theorem, reduction, or calculation involved. Verified corrections will be assessed and attribution updated where justified.

## References

1. **Masamichi Iizumi** (2026), *Binary convolution height: Structural invariants of integer factorisations*, *Research in Mathematics*, 13(1), Article 2727395, Definition 4, Proposition 1 and Question 3. https://doi.org/10.1080/27684830.2026.2727395
2. **David Eppstein** (2021), *Carrying as chip-firing for the Zeckendorf representation*, including “Binary carrying as chip-firing”. https://11011110.github.io/blog/2021/06/12/carrying-chip-firing.html
3. **A. Izsak and N. Pippenger** (2011), *Carry propagation in multiplication by constants*, *ACM Transactions on Algorithms*, 7(4). https://arxiv.org/abs/0801.4040
4. **C. Heuberger, S. Kropf and H. Prodinger** (2017), *Analysis of carries in signed digit expansions*, *Monatshefte für Mathematik*. https://arxiv.org/abs/1503.08816
5. **A. Kruppa** (2010), *Speeding up Integer Multiplication and Factorization*, doctoral thesis. https://docnum.univ-lorraine.fr/public/SCD_T_2010_0054_KRUPPA.pdf
