# The Jhon Pulgarin Model: Spatial Discontinuity

Treatise on Spatial Discontinuity and the Architectural Zero

## Index

1. [Historical Introduction](#1-historical-introduction)
2. [Case Study: The Elevator](#2-case-study-the-elevator)
3. [Statement of the Model](#3-statement-of-the-model)
4. [Formal Proof](#4-formal-proof)
5. [Properties Derived from the Model](#5-properties-derived-from-the-model)
6. [Complete Examples](#6-complete-examples)
7. [Applications of the Method](#7-applications-of-the-method)
8. [Final Conclusion](#8-final-conclusion)
9. [Historical Background and Related Work](#9-historical-background-and-related-work)
10. [Formal Verification of Methods](#10-formal-verification-of-methods-theorem-prover-via-smt-solver)

---

## 1. HISTORICAL INTRODUCTION

#### 1. Introduction and Historical Context: A Problem of Centuries

The contradiction between abstract counting and physical reality is not a modern confusion. It is a logical dilemma with centuries of history that affects the way human beings organize time, space, and information. The main origin of this conflict lies in the historical difficulty of accepting and integrating the concept of 'zero' as a physical entity and not just a mathematical one.

The clearest example of this is found in our current calendar. The chronological system passes directly from the year 1 before Christ (B.C.) to the year 1 after Christ (A.D.). Physically, the 'year zero' never existed in official history. This means that, when calculating the time elapsed between the year 1 B.C. and the year 1 A.D., pure mathematics, by treating the years as integers on a continuous number line, yields a distance of 2 units (calculating $|1 - (-1)| = 2$). However, the real timeline has no year 0, so the real distance is 1 unit: the year 1 A.D. is immediately consecutive to the year 1 B.C.

#### 2. The Logical Discrepancy: Mathematicians vs. Programmers

This historical mismatch has sparked a classic debate in the world of science and technology, dividing logic into two well-defined camps:

- **The Pure Mathematical Approach:** Mathematicians operate under a continuous number line where zero is indispensable. For abstract mathematics, zero represents the point of origin or equilibrium. When applying continuous number-line models without adapting the chronological convention, calculations can produce distances that do not match physical reality, artificially inflating perceived distances.

- **The Programming and Engineering Approach:** Software developers and engineers constantly run into this through the famous 'Fencepost Error' and, in a related but distinct way, zero-based indexing problems (in languages such as C, Python, or Java, where arrays start at 0 and not at 1). A programmer knows that one thing is the number of intermediate elements and quite another is the index of the positions, requiring conversions when interacting with human interfaces that use one-based numbering, so that applications do not fail when mapping the real world.

---

## 2. CASE STUDY: THE ELEVATOR

#### The Case Study: The Elevator Dilemma

The Jhon Pulgarín Model is born from the direct observation of this phenomenon in everyday architecture: a person lives on floor 2 and their parking spot is in basement 1. How many floors separate their home from their parking spot?

If this problem is introduced in a linear fashion into an Artificial Intelligence or a theoretical mathematical system that treats floors as integers on a continuous number line (where basement 1 is represented as $-1$), strict mathematical calculation establishes that the distance is 3 (calculating $2 - (-1) = 3$). However, in real life, the elevator buttons in that building show that going down from floor 2 to basement 1 involves only 2 buttons.

#### The Official Formula of the Model

$$O = |\text{index}(A) - \text{index}(B)| - 1$$

Where:

- $O$ = Number of things that are IN BETWEEN $A$ and $B$, without counting $A$ or $B$.
- $\text{index}(A)$ = Position of the first element.
- $\text{index}(B)$ = Position of the second element.
- $| \ |$ = Absolute value.
- $-1$ = Because subtracting indices counts one endpoint, minus one corrects everything.

---

## 3. STATEMENT OF THE MODEL

Given any two positions $A$ and $B$ mapped in a discrete sequential space, with positions indexed as $\text{index}(A)$ and $\text{index}(B)$, the number of strictly intermediate elements (excluding both endpoints) is defined by the counting function:

$$O = |\text{index}(A) - \text{index}(B)| - 1$$

Where $O$ represents the cardinality of the subset of internal elements that separate $A$ from $B$.

---

## 4. FORMAL PROOF

1. The indexed transition distance between both positions is defined by the absolute metric: $D = |\text{index}(A) - \text{index}(B)|$.

2. By definition of discrete distance, the value $D$ represents the absolute distance between both positions on the indexed scale, equivalent to the number of steps needed to go from one to the other.

3. To isolate exclusively the open interval $(\text{index}(A), \text{index}(B))$, the destination element ($B$) must be removed from the total count.

4. Substituting the exclusion restriction into the original metric yields: $O = D - 1 = |\text{index}(A) - \text{index}(B)| - 1$. *Quod Erat Demonstrandum* (Q.E.D.).

---

## 5. PROPERTIES DERIVED FROM THE MODEL

- **Contiguity Condition:** If $A$ and $B$ are consecutive adjacent elements, then $O = 1 - 1 = 0$ (zero intermediate elements).

- **Vacuity Identity:** If $A = B$, the model is undefined (or requires a boundary condition), since the formula yields $O = 0 - 1 = -1$, a value with no physical interpretation. In practice, $A \neq B$ is assumed.

- **Bounded Non-Negativity:** $O \geq 0$ for any pair of distinct and non-consecutive positions in the indexed space. The case $A = B$ is excluded from this property because it is a degeneration of the model.

- **Directional Symmetry:** The use of the absolute value guarantees that $O(A,B) = O(B,A)$, proving that the count is invariant with respect to the direction of navigation.

---

## 6. COMPLETE EXAMPLES

#### 1. Elevator Problem (Floor 2 to B1)

An elevator is on floor 2 and must go down to B1 (Basement 1). It is required to know how many floors separate them, without counting the origin floor or the destination floor.

##### Data

To avoid "phantom floors", we assign real consecutive indices:

- **Floor A (origin):** Floor 2 → index $2$
- **Floor B (destination):** Basement 1 → index $0$
  *(Note: The intermediate Floor 1 occupies index 1)*

##### Formula and development

First we find the total distance ($D$):

$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |2 - 0|$$
$$D = |2| = 2$$

Now we find the intermediate floors ($O$):

$$O = D - 1$$
$$O = 2 - 1 = 1$$

##### Answer

It is separated by **1 single intermediate floor**, which is **Floor 1**.

---

#### 2. Problem of the Jars

##### Problem statement

There are 5 jars in a row numbered from 1 to 5. Jar 1 and jar 5 are the extremes. It is required to know how many jars are between them, without counting the origin or the destination.

##### Data

Since the jars in the physical world are already consecutive by nature, their numbers are equivalent to their indices:

- **Jar A (origin):** Jar 1 → index $1$
- **Jar B (destination):** Jar 5 → index $5$

##### Formula and development

First we find the total distance ($D$):

$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |1 - 5|$$
$$D = |-4| = 4$$

Now we find the intermediate jars ($O$):

$$O = D - 1$$
$$O = 4 - 1 = 3$$

##### Answer

They are separated by **3 intermediate jars**, which are **2, 3, and 4**.

---

#### 3. Problem of the Eras (1 B.C. and 1 A.D.)

##### Problem statement

It is required to know how many complete years are between the year 1 B.C. and the year 1 A.D., without counting the origin year or the destination year.

##### Data

Given that in conventional historical chronology **the year 0 does not exist** (the year 1 A.D. began immediately after the year 1 B.C. ended), we assign real consecutive indices to reflect this continuity:

- **Year A (origin):** 1 B.C. → index $0$
- **Year B (destination):** 1 A.D. → index $1$

##### Formula and development

First we find the total distance ($D$):

$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |0 - 1|$$
$$D = |-1| = 1$$

Now we find the intermediate years ($O$):

$$O = D - 1$$
$$O = 1 - 1 = 0$$

##### Answer

They are separated by **0 intermediate years**. The year 1 A.D. is immediately consecutive to the year 1 B.C.

---

### PYTHON SCRIPT

```python
def calculate_intermediate_elements(index_a, index_b):
    """
    Applies the universal formula: O = |index(A) - index(B)| - 1
    """
    distance = abs(index_a - index_b)
    intermediates = distance - 1
    return intermediates


# =====================================================================
# 1. ELEVATOR PROBLEM (Floor 2 to Basement 1 - No Ground Floor)
# Real continuous scale: B1 = 0, Floor 1 = 1, Floor 2 = 2
# =====================================================================
floor_origin_idx = 2   # Floor 2
floor_destination_idx = 0  # Basement 1

intermediate_floors = calculate_intermediate_elements(floor_origin_idx, floor_destination_idx)

print("--- 1. ELEVATOR PROBLEM ---")
print(f"Origin Index (Floor 2): {floor_origin_idx}")
print(f"Destination Index (B1): {floor_destination_idx}")
print(f"Real intermediate floors separating them: {intermediate_floors}\n")


# =====================================================================
# 2. PROBLEM OF THE JARS IN A ROW
# Scale: Jar 1 = 1, Jar 5 = 5
# =====================================================================
jar_origin_idx = 1
jar_destination_idx = 5

intermediate_jars = calculate_intermediate_elements(jar_origin_idx, jar_destination_idx)

print("--- 2. PROBLEM OF THE JARS ---")
print(f"Origin Index (Jar 1): {jar_origin_idx}")
print(f"Destination Index (Jar 5): {jar_destination_idx}")
print(f"Real intermediate jars separating them: {intermediate_jars}\n")


# =====================================================================
# 3. PROBLEM OF THE ERAS (1 B.C. to 1 A.D. - No Historical Year 0)
# Real continuous scale: 1 B.C. = 0, 1 A.D. = 1
# =====================================================================
year_origin_idx = 0   # 1 B.C.
year_destination_idx = 1  # 1 A.D.

intermediate_years = calculate_intermediate_elements(year_origin_idx, year_destination_idx)

print("--- 3. PROBLEM OF THE ERAS ---")
print(f"Origin Index (1 B.C.): {year_origin_idx}")
print(f"Destination Index (1 A.D.): {year_destination_idx}")
print(f"Real intermediate years separating them: {intermediate_years}\n")
```

---

## 7. APPLICATIONS OF THE METHOD

- **Data Structures and Arrays** (calculation of logical distances and offsets)
- **Node Management** in linked lists and linear structures
- **Theory of Open Intervals** and cardinality of discrete sets
- **Combinatorial Counting** and analysis of numerical sequences
- **Software Development** (native solution to the *Fencepost Error*)
- **Chronology Systems** and time organization without Year 0
- **Civil Engineering and Architecture** (logical mapping of elevators without Floor 0)

---

## 8. FINAL CONCLUSION

The formalization of the calculation through $O = |\text{index}(A) - \text{index}(B)| - 1$ successfully decouples software logic from the irregularities of physical nomenclature. By mapping a discontinuous space into a sequentially indexed array, the need for complex conditionals (`if/else`) to handle exceptions such as the absence of floor zero is eliminated.

This transforms a spatial arithmetic problem into a constant-time operation $O(1)$ over indices, guaranteeing a robust, predictable, and easily scalable navigation model for any architectural configuration.

---

## 9. HISTORICAL BACKGROUND AND RELATED WORK

The present Jhon Pulgarín Model formally addresses a phenomenon identified in various scientific disciplines throughout history. Although the underlying logic of the cardinality of open intervals is universal, its systematic application connects directly with the following milestones in science and technology:

### A. Discrete Mathematics: Cardinality of Open Intervals

In set theory and enumerative combinatorics, the calculation of strictly internal elements between two integer bounds $A$ and $B$ (where $A < B$) is formally defined as the cardinality of an open interval $(A, B)$. The use of the absolute value $|\text{index}(A) - \text{index}(B)| - 1$ extends this notion, making it symmetric and applicable regardless of the direction of the vectorized traversal, eliminating sign dependencies in the measurement of discrete distances.

### B. Computer Science: Edsger Dijkstra and the "Fencepost Error"

In software engineering, the core of this abstraction solves the classic Fencepost Error (*Off-by-one Error*). In the 1970s, computer scientist Edsger Dijkstra formalized the advantages of zero-based indexing to ensure that range and interval operations in computer memory were consistent, avoiding manual arithmetic corrections when iterating over data subsets.

### C. Astronomy: Jacques Cassini and the Introduction of Year 0

The mismatch analyzed in the transition between discontinuous scales (such as the direct step from 1 B.C. to 1 A.D.) was physically addressed by the French astronomer Jacques Cassini in 1740. Cassini identified that mathematical calculations for predicting historical eclipses failed by a factor of one year due to the nonexistence of year 0 in traditional calendars. To solve this, he introduced the "Astronomical Year" scale, where the year 1 B.C. is numerically denoted as year 0, validating the need to implement continuous indices to map physical reality.

---

## 10. FORMAL VERIFICATION OF METHODS (THEOREM PROVER VIA SMT SOLVER)

The mathematical property of symmetry of the formula is formally proven for the infinite universe of integers. Instead of relying solely on empirical simulations or random sampling prone to missing edge cases, the methodological framework incorporates an Automated Theorem Prover powered by Microsoft Research's Z3 SMT solver.

This engine algebraically evaluates the constraints, proving that no mathematical counterexample exists where the direction of traversal affects the result, establishing absolute certainty for the indexing model.

```python
def run_formal_smt_verification():
    print("----------------------------------------------------")
    print("  REAL FORMAL VERIFICATION (Z3 SMT SOLVER)")
    print("----------------------------------------------------")
    try:
        from z3 import Solver, Int, Abs as z3_abs, unsat

        solver = Solver()
        a = Int('a')
        b = Int('b')

        # We define the mathematical formula for Z3
        formula_a_b = z3_abs(a - b) - 1
        formula_b_a = z3_abs(b - a) - 1

        # We ask Z3 to look for a COUNTEREXAMPLE:
        # "Find some case where formula_a_b is DIFFERENT from formula_b_a"
        solver.add(formula_a_b != formula_b_a)

        # If the result is UNSAT (unsatisfiable), it means NO counterexample exists
        if solver.check() == unsat:
            print("✅ FORMAL VERIFICATION SUCCESSFUL: Z3 mathematically proved")
            print("   that the symmetry property holds for the infinity of integers.")
        else:
            print("❌ A counterexample was found (the formula failed).")

    except ImportError:
        print("ℹ️ Run `pip install z3-solver` to execute the real mathematical verification.")

run_formal_smt_verification()
```

---

Jhon Pulgarin - 2026 Villavicencio, Meta - Colombia
