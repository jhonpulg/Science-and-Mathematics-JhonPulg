# Jhon Pulgarin's Theorem and the spatial discontinuity of the architectural zero

**Treatise on Spatial Discontinuity and the Architectural Zero**

---

### 1. HISTORICAL INTRODUCTION

1. Introduction and Historical Context: A Centuries-Old Problem
The contradiction between abstract counting and physical reality is not a modern confusion. It is a logical dilemma with centuries of history that affects the way human beings organize time, space, and information. The main origin of this conflict lies in the historical difficulty in accepting and integrating the concept of 'zero' as a physical entity and not just a mathematical one.
The clearest example of this is found in our current calendar. The chronological system goes directly from the year 1 Before Christ (B.C.) to the year 1 Anno Domini (A.D.). Physically, the 'year zero' never existed in official history. This generates that, when calculating the time elapsed between the year 1 B.C. and the year 1 A.D., pure mathematics dictates a distance of 2 units, when in the real timeline there is only a change of era with no year in between.

2. The Logical Discrepancy: Mathematicians vs. Programmers
This historical gap has caused a classic debate in the world of science and technology, dividing logic into two well-defined camps:
• The Pure Mathematical Approach: Mathematicians operate under a continuous number line where zero is indispensable. For abstract mathematics, zero represents the point of origin or equilibrium. By ignoring whether zero has a real physical representation, their calculations always assume an intermediate space that artificially increases physical distances.
• The Programming and Engineering Approach: Software developers and engineers constantly clash with this through the famous 'Fencepost Error' or zero-based indexing problems (where lists start at 0 and not 1). A programmer knows that one thing is the number of intermediate elements and a very different thing is the index of the positions, requiring constant adjustments in the code so that applications do not fail when interacting with the real world.

### 2. CASE STUDY: THE ELEVATOR
The Case Study: The Elevator Dilemma case why Jhon Pulgarin found the problem with 0
Jhon Pulgarin's Theory is born from direct observation of this phenomenon in everyday architecture:
A person lives on floor 2 and his parking space is in basement 1. How many floors separate his home from his parking space?
If this problem is introduced linearly into an Artificial Intelligence or a theoretical mathematical system, the strict mathematical calculation establishes that the distance is 3 (calculating 2 - (-1) = 3). However, in real life, the elevator buttons in that building show that when going down from floor 2 to basement 1 there are only 2 buttons
                     OFFICIAL FORMULA

O = |index(A) - index(B)| - 1

Where:
- O = Quantity of things that are IN BETWEEN A and B, not counting A nor B.
- index(A) = Position of the first element
- index(B) = Position of the second element
- | | = Absolute value
- -1 = Because when subtracting indices you count one extreme, minus one corrects everything

### 3. MODEL STATEMENT

Given any two positions $A$ and $B$ mapped within a sequential discrete space, 
with indexed positions denoted as $\text{index}(A)$ and $\text{index}(B)$, the 
number of strictly intermediate elements (excluding both endpoints) is defined 
by the ordering function:

$$O = |\text{index}(A) - \text{index}(B)| - 1$$

Where $O$ represents the cardinality of the subset of internal elements that 
separate $A$ from $B$.

### 4. FORMAL PROOF

1. The indexed transition distance between both positions is defined by the 
   absolute metric: $D = |\text{index}(A) - \text{index}(B)|$.
2. By definition of discrete distance, the value $D$ counts all the steps 
   required to reach the final position, excluding the origin $A$ but 
   including the destination $B$.
3. To exclusively isolate the open interval $(\text{index}(A), \text{index}(B))$, 
   the destination element ($B$) must be removed from the total count.
4. Substituting the exclusion constraint into the original metric yields: 
   $O = D - 1 = |\text{index}(A) - \text{index}(B)| - 1$. *Quod Erat Demonstrandum* (Q.E.D.).

### 5. DERIVED MODEL PROPERTIES

* **Contiguity Condition:** If $A$ and $B$ are adjacent consecutive elements, 
  then $O = 1 - 1 = 0$ (zero intermediate elements).
* **Identity of Vacuity:** If $A = B$, then $O = 0 - 1 = -1$, which formalizes a 
  nonexistent or null interval by discrete topological definition.
* **Bounded Non-Negativity:** $O \geq 0$ for any pair of distinct, non-consecutive 
  positions within the indexed space.
* **Directional Symmetry:** The use of the absolute value guarantees that 
  $O(A,B) = O(B,A)$, proving that the count is invariant with respect to the 
  direction of navigation.


## 6. COMPLETE EXAMPLES

### 1. Elevator Problem (Floor 2 to B1)
An elevator is on floor 2 and must go down to B1 (Basement 1). It is required to know how many floors separate them, not counting the origin floor nor the destination floor.

### Data
To avoid "ghost floors", we assign real consecutive indices:
* **Floor A (origin):** Floor 2 $\rightarrow$ index $2$
* **Floor B (destination):** Basement 1 $\rightarrow$ index $0$
*(Note: The intermediate Floor 1 occupies index 1)*

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |2 - 0|$$
$$D = |2| = 2$$

Now we find the intermediate floors ($O$):
$$O = D - 1$$
$$O = 2 - 1 = 1$$

### Answer
It is separated by **only 1 intermediate floor**, which is **Floor 1**.

---

## 2. Pots Problem

### Problem statement
There are 5 pots in a row numbered from 1 to 5. Pot 1 and pot 5 are the extremes. It is required to know how many pots are between them, not counting the origin nor the destination.

### Data
Since the pots in the physical world are already consecutive by nature, their numbers are equivalent to their indices:
* **Pot A (origin):** Pot 1 $\rightarrow$ index $1$
* **Pot B (destination):** Pot 5 $\rightarrow$ index $5$

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |1 - 5|$$
$$D = |-4| = 4$$

Now we find the intermediate pots ($O$):
$$O = D - 1$$
$$O = 4 - 1 = 3$$

### Answer
They are separated by **3 intermediate pots**, which are **2, 3 and 4**.

---

## 3. Eras Problem (1 B.C. and 1 A.D.)

### Problem statement
It is wanted to know how many full years are between the year 1 B.C. and the year 1 A.D., not counting the year of origin nor the destination.

### Data
Given that in conventional historical chronology **year 0 does not exist** (year 1 A.D. began immediately after year 1 B.C. ended), we assign real consecutive indices to reflect this continuity:
* **Year A (origin):** 1 B.C. $\rightarrow$ index $0$
* **Year B (destination):** 1 A.D. $\rightarrow$ index $1$

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |0 - 1|$$
$$D = |-1| = 1$$

Now we find the intermediate years ($O$):
$$O = D - 1$$
$$O = 1 - 1 = 0$$

### Answer
They are separated by **0 intermediate years**. Year 1 A.D. is immediately consecutive to year 1 B.C.

### Real Historical Adjustment
The mathematical formula yields a theoretical result of 1 intermediate year (which would correspond to year 0). However, in the Christian historical and chronological record **year 0 does not exist**. Year 1 A.D. follows immediately after year 1 B.C.

Therefore, in historical reality:
$$O = 0$$

### Answer
In chronological reality, **0 full years** separate year 1 B.C. from year 1 A.D.

### PYTHON SCRIPT

```python
def calculate_intermediate_elements(index_a, index_b):
    """
    Applies the universal formula: O = |index(A) - index(B)| - 1
    """
    distance = abs(index_a - index_b)
    intermediate = distance - 1
    return intermediate

# =====================================================================
# 1. ELEVATOR PROBLEM (Floor 2 to Basement 1 - Without Ground Floor)
# Real continuous scale: B1 = 0, Floor 1 = 1, Floor 2 = 2
# =====================================================================
origin_floor_idx = 2  # Floor 2
destination_floor_idx = 0  # Basement 1

intermediate_floors = calculate_intermediate_elements(origin_floor_idx, destination_floor_idx)

print("--- 1. ELEVATOR PROBLEM ---")
print(f"Origin Index (Floor 2): {origin_floor_idx}")
print(f"Destination Index (B1): {destination_floor_idx}")
print(f"Real intermediate floors separating them: {intermediate_floors}\n")

# =====================================================================
# 2. POTS IN A ROW PROBLEM
# Scale: Pot 1 = 1, Pot 5 = 5
# =====================================================================
origin_pot_idx = 1
destination_pot_idx = 5

intermediate_pots = calculate_intermediate_elements(origin_pot_idx, destination_pot_idx)

print("--- 2. POTS PROBLEM ---")
print(f"Origin Index (Pot 1): {origin_pot_idx}")
print(f"Destination Index (Pot 5): {destination_pot_idx}")
print(f"Real intermediate pots separating them: {intermediate_pots}\n")

# =====================================================================
# 3. ERAS PROBLEM (1 B.C. to 1 A.D. - Without Historical Year 0)
# Real continuous scale: 1 B.C. = 0, 1 A.D. = 1
# =====================================================================
origin_year_idx = 0  # 1 B.C.
destination_year_idx = 1  # 1 A.D.

intermediate_years = calculate_intermediate_elements(origin_year_idx, destination_year_idx)

print("--- 3. ERAS PROBLEM ---")
print(f"Origin Index (1 B.C.): {origin_year_idx}")
print(f"Destination Index (1 A.D.): {destination_year_idx}")
print(f"Real intermediate years separating them: {intermediate_years}\n")
```
### 7. APPLICATIONS OF THE THEOREM

1.  Data structures and Arrays
2.  Linked lists
3.  Open interval theory and sets
4.  Combinatorial counting and Sequence analysis
5.  Programming (solves Fencepost Error)
6.  Time and space organization
7.  Civil Engineering and Architecture

### 8. FINAL CONCLUSION

# Technical Conclusion: Spatial Navigation via Index Abstraction

Formalizing the calculation using $O = |\text{index}(A) - \text{index}(B)| - 1$ successfully decouples 
software logic from the irregularities of physical naming conventions. By mapping a 
discontinuous space into a sequentially indexed array, the need for complex conditional 
statements (`if/else`) to handle exceptions—such as the absence of a ground floor—is 
entirely eliminated. 

This transforms a spatial arithmetic problem into a constant-time $O(1)$ index operation, 
ensuring a robust, predictable, and highly scalable navigation model for any 
architectural layout.


### 9. HISTORICAL BACKGROUND AND RELATED WORK


The present indexing model formally addresses a phenomenon identified across various scientific 
disciplines throughout history. Although the underlying logic of open interval cardinality 
is universal, its systematic application connects directly with the following milestones 
in science and technology:

### A. Discrete Mathematics: Open Interval Cardinality
In set theory and enumerative combinatorics, the calculation of strictly internal elements 
between two integer bounds $A$ and $B$ (where $A < B$) is formally defined as the cardinality 
of an open interval $(A, B)$. The use of the absolute value $|\text{index}(A) - \text{index}(B)| - 1$ 
extends this notion, making it symmetrical and applicable regardless of the direction of the 
vectorized traversal, thereby eliminating sign dependencies in discrete distance measurement.

### B. Computer Science: Edsger Dijkstra and the "Fencepost Error"
In software engineering, the core of this abstraction resolves the classic Fencepost Error 
(or Off-by-one Error). In the 1970s, computer scientist Edsger Dijkstra formalized the 
advantages of zero-based indexing to ensure that range and interval operations in computer 
memory remained consistent, avoiding manual arithmetic corrections when iterating over data 
subsets.

### C. Astronomy: Jacques Cassini and the Introduction of Year 0
The discrepancy analyzed in the transition of discontinuous scales (such as the direct shift 
from 1 BC to 1 AD) was physically addressed by the French astronomer Jacques Cassini in 1740. 
Cassini identified that mathematical calculations for predicting historical eclipses failed 
by a factor of one year due to the nonexistence of Year 0 in traditional calendars. To 
resolve this, he introduced the "Astronomical Year Numbering" scale, where 1 BC is denoted 
numerically as year 0, validating the need to implement continuous indices to map physical reality.


### 10. FORMAL VERIFICATION OF METHODS (THEOREM PROVER VIA SMT SOLVER)


The mathematical property of symmetry in the formula is formally proven for the infinite 
universe of integers. Instead of relying solely on empirical simulations or random 
sampling prone to missing edge cases, the methodological framework incorporates an 
Automated Theorem Prover powered by the Z3 SMT solver from Microsoft Research. 

This engine algebraically evaluates the constraints, proving that no mathematical 
counterexample exists where the direction of travel affects the outcome, thereby 
establishing absolute certainty for the indexing model.



```python
def run_formal_verification_smt():
    print("----------------------------------------------------")
    print("  REAL FORMAL VERIFICATION (Z3 SMT SOLVER)")
    print("----------------------------------------------------")
    try:
        from z3 import Solver, Int, Abs as z3_abs, unsat
        
        solver = Solver()
        a = Int('a')
        b = Int('b')
        
        # Define the mathematical formula for Z3
        formula_a_b = z3_abs(a - b) - 1
        formula_b_a = z3_abs(b - a) - 1
        
        # Ask Z3 to find a COUNTEREXAMPLE:
        # "Find any case where formula_a_b is NOT EQUAL to formula_b_a"
        solver.add(formula_a_b != formula_b_a)
        
        # If the result is UNSAT (unsatisfiable), it means NO counterexample exists
        if solver.check() == unsat:
            print("✅ FORMAL VERIFICATION SUCCESSFUL: Z3 mathematically proved")
            print("   that the symmetry property holds for the infinity of integers.")
        else:
            print("❌ A counterexample was found (the formula failed).")
            
    except ImportError:
        print("ℹ️ Run `pip install z3-solver` to execute the real mathematical verification.")

run_formal_verification_smt()

```

---
**Jhon Pulgarin - 2026**
**Villavicencio, Meta - Colombia**


