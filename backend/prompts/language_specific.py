"""
Language-specific prompt enhancements.
These are added to the base prompt to provide language-specific guidance.
"""

PYTHON_PROMPT = """When reviewing Python code, pay special attention to:

**Pythonic Code:**
- Use of list/dict comprehensions where appropriate
- Proper use of generators and iterators
- Context managers (with statements)
- Decorators and their use cases
- Type hints (PEP 484) for better code clarity

**Common Patterns:**
- EAFP vs LBYL (Easier to Ask for Forgiveness vs Look Before You Leap)
- Duck typing and when to use it
- Proper exception handling hierarchy
- Using built-in functions (map, filter, zip, enumerate)

**Best Practices:**
- PEP 8 style guide compliance
- Meaningful variable names (snake_case)
- Docstrings (Google or NumPy style)
- Virtual environments and dependency management
- Using `if __name__ == "__main__":` properly

**Common Pitfalls:**
- Mutable default arguments
- Late binding closures
- Understanding the difference between `is` and `==`
- Global vs local scope issues
- Memory leaks with circular references

**Ask about:**
- Why they chose a particular approach
- If they considered more Pythonic alternatives
- Whether they need the code to be more performant
- Testing strategy (pytest, unittest)"""


JAVASCRIPT_PROMPT = """When reviewing JavaScript code, pay special attention to:

**Modern JavaScript (ES6+):**
- Use of const/let vs var
- Arrow functions and their context binding
- Destructuring for cleaner code
- Template literals
- Spread operator and rest parameters
- Promises and async/await vs callbacks

**Common Patterns:**
- Closures and their practical uses
- Event loop understanding
- Prototypal inheritance vs classes
- Module patterns (ESM vs CommonJS)
- Callbacks vs Promises vs async/await

**Best Practices:**
- Avoiding callback hell
- Proper error handling with try/catch and .catch()
- Using strict mode
- Avoiding global variables
- Understanding `this` context
- Immutability principles

**Common Pitfalls:**
- Type coercion issues (== vs ===)
- `this` binding confusion
- Asynchronous code gotchas
- Memory leaks (event listeners, closures)
- Truthy/falsy values misunderstanding

**Ask about:**
- Browser vs Node.js environment
- Whether they're using a framework (React, Vue, etc.)
- Testing approach (Jest, Mocha)
- Bundler/transpiler setup (Webpack, Babel)"""


TYPESCRIPT_PROMPT = """When reviewing TypeScript code, pay special attention to:

**Type System:**
- Proper use of interfaces vs types
- Generic types and constraints
- Union and intersection types
- Type guards and narrowing
- Utility types (Partial, Pick, Omit, etc.)
- Avoiding `any` - using `unknown` when necessary

**Best Practices:**
- Strict mode enabled in tsconfig.json
- Proper type annotations (not over-annotating)
- Using enums appropriately
- Discriminated unions for variants
- Type inference leverage
- Readonly properties and arrays

**Common Patterns:**
- Conditional types
- Mapped types
- Type assertion vs type casting
- Decorator usage (experimental)
- Namespace vs module organization

**Common Pitfalls:**
- Over-using `any` or `as`
- Not understanding structural typing
- Ignoring compiler errors with `@ts-ignore`
- Not leveraging type inference
- Complex types that hurt readability

**Ask about:**
- Their tsconfig.json settings
- Whether types help or hinder their workflow
- Testing strategy with types (Jest with ts-jest)
- Integration with frameworks (React, Angular, etc.)"""


JAVA_PROMPT = """When reviewing Java code, pay special attention to:

**Object-Oriented Design:**
- SOLID principles application
- Proper use of inheritance vs composition
- Interface vs abstract class usage
- Access modifiers (private, protected, public)
- Static vs instance members

**Best Practices:**
- Naming conventions (PascalCase for classes, camelCase for methods)
- Package organization
- Exception handling (checked vs unchecked)
- Resource management (try-with-resources)
- Immutability with final keyword
- Using Optional instead of null

**Modern Java (8+):**
- Streams API and functional programming
- Lambda expressions
- Method references
- Default methods in interfaces
- var keyword (Java 10+)

**Common Patterns:**
- Singleton, Factory, Builder patterns
- Dependency Injection
- MVC/MVVM architecture
- DAO pattern for data access

**Common Pitfalls:**
- NullPointerException handling
- Memory leaks (unclosed resources)
- String concatenation in loops
- Overuse of inheritance
- Not overriding equals/hashCode properly

**Ask about:**
- Which Java version they're using
- Build tool (Maven, Gradle)
- Framework usage (Spring, Jakarta EE)
- Testing approach (JUnit, Mockito)"""


CPP_PROMPT = """When reviewing C++ code, pay special attention to:

**Memory Management:**
- Proper use of RAII (Resource Acquisition Is Initialization)
- Smart pointers (unique_ptr, shared_ptr, weak_ptr)
- Avoiding memory leaks and dangling pointers
- Understanding the stack vs heap
- Move semantics and std::move

**Modern C++ (11/14/17/20):**
- Auto keyword for type inference
- Range-based for loops
- nullptr instead of NULL
- constexpr for compile-time evaluation
- Lambda expressions
- Structured bindings

**Best Practices:**
- Rule of Three/Five/Zero
- const correctness
- Initialization (uniform initialization with {})
- Avoiding raw pointers when possible
- Header guards or #pragma once
- Namespace usage

**Performance:**
- Pass by reference vs value vs pointer
- RVO and copy elision
- Inline functions appropriately
- Template metaprogramming basics
- Cache-friendly code

**Common Pitfalls:**
- Memory leaks and undefined behavior
- Use after free
- Buffer overflows
- Uninitialized variables
- Shallow vs deep copy issues

**Ask about:**
- C++ standard they're targeting
- Compiler and flags used
- Build system (CMake, Make)
- Platform-specific concerns"""


GO_PROMPT = """When reviewing Go code, pay special attention to:

**Go Idioms:**
- Error handling with multiple return values
- Defer statements for cleanup
- Goroutines and channels for concurrency
- Empty interface{} usage (vs any in Go 1.18+)
- Struct embedding vs composition

**Best Practices:**
- Effective Go guidelines
- Naming conventions (MixedCaps)
- Package organization
- Error wrapping with fmt.Errorf and %w
- Using context.Context for cancellation
- Interface design (small, focused interfaces)

**Concurrency:**
- Proper goroutine lifecycle management
- Channel patterns (fan-in, fan-out)
- Avoiding goroutine leaks
- Mutex vs channels for synchronization
- Context for timeout and cancellation

**Common Patterns:**
- Constructor functions (NewXxx)
- Functional options pattern
- Table-driven tests
- Error handling patterns

**Common Pitfalls:**
- Goroutine leaks
- Race conditions (use -race flag)
- Closing channels incorrectly
- Pointer vs value receivers
- Ignoring errors

**Ask about:**
- Go version (generics in 1.18+?)
- Module system understanding
- Testing approach (table tests)
- Deployment target (single binary advantage)"""


RUST_PROMPT = """When reviewing Rust code, pay special attention to:

**Ownership & Borrowing:**
- Ownership rules understanding
- Borrowing (& and &mut) usage
- Lifetimes and when to annotate
- Moving vs copying vs cloning
- Reference counting with Rc/Arc

**Safety & Correctness:**
- Pattern matching exhaustiveness
- Option and Result types instead of null/exceptions
- Proper error handling with ? operator
- Avoiding unwrap() in production
- Safe vs unsafe code boundaries

**Best Practices:**
- Idiomatic Rust (clippy suggestions)
- Naming conventions (snake_case)
- Module organization
- Documentation comments (///)
- Using cargo fmt and clippy
- Iterator methods over loops

**Concurrency:**
- Send and Sync traits
- Arc and Mutex for shared state
- Channels (mpsc, crossbeam)
- async/await with tokio or async-std
- Data races prevented by compiler

**Common Patterns:**
- Builder pattern with typestate
- Newtype pattern
- RAII with Drop trait
- Trait objects vs generics
- Error handling with thiserror/anyhow

**Common Pitfalls:**
- Fighting the borrow checker
- Overusing .clone()
- Not understanding lifetimes
- Confusing String vs &str
- Panic in production code

**Ask about:**
- Rust edition (2018, 2021)
- Async runtime if applicable
- Crate dependencies
- Target platform considerations"""
