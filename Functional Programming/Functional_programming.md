## Functional Programming:
<P>Functional programming is a programming paradigm that focuses on:</P>
<P>Separation of Concerns: It organizes code into functions and data structures, ensuring that each function has a single, well-defined purpose.</P>
<P>Separation of Data and Behavior: Unlike OOP, which combines methods (behavior) and attributes (data) into objects, FP treats data and functions as separate entities. Functions operate on data but don’t own or encapsulate it.</P>

### FP and OOP
**OOP:** Encapsulation is a key principle. Data (attributes) and behavior (methods) are bundled together in objects. For example:
+ Wizard and Archer classes in OOP contain both attributes (e.g., health, mana) and methods (e.g., attack, defend).
**FP:** Instead of combining methods and attributes, FP separates them:</p>
+ Data is represented in simple structures like lists or dictionaries.
+ Functions perform actions on the data, independent of the data's structure.

### Principles of Functional Programming

#### Pure Functions:
+ A pure function always produces the same output given the same input.
+ It has no side effects (e.g., modifying a global variable or I/O operations).
+ This predictability makes code easier to test and reason about.

#### Immutability:
+ Data in FP is typically immutable, meaning once created, it cannot be modified.
+ Instead of changing data, new copies are created with the desired updates.

#### First-Class and Higher-Order Functions:
+ Functions are treated as first-class citizens, meaning they can be passed as arguments, returned from other functions, and assigned to variables.
+ Higher-order functions operate on other functions (e.g., map, filter, reduce).

#### Declarative Approach:
+ FP emphasizes describing what to do rather than how to do it, contrasting the step-by-step instructions in imperative programming.

#### Avoidance of Shared State:
+ Functions do not rely on or alter shared state, reducing potential bugs from unintended interactions.

Comparison of FP and OOP Goals:
#### Despite their differences, FP and OOP share common objectives:
+ Code Organization: Both aim to make code modular, clean, and maintainable.
+ Reusability: Both encourage reuse of code (e.g., through classes in OOP or functions in FP).
+ Scalability: Both paradigms support growing and extending codebases over time.
+ DRY Principle: Both promote avoiding redundancy in code.


#### Why Choose FP?
+ Simplifies reasoning about code due to the emphasis on pure functions and immutability.
+ Makes debugging and testing easier since pure functions are isolated from external effects.
+ Fits well with parallel and concurrent programming due to the avoidance of shared state.
