"""5.Explain the difference between how Python executes code versus how C or 
Java executes code, using your own words and a simple example for each.


1. C: Direct Compilation (Machine Code)
    How it works: 
        
        -C is a compiled language. A C compiler reads your entire source code file, 
        checks for errors, and translates it directly into native machine code 
        tailored to a specific operating system and processor architecture 
        (like x86 or ARM).
    
    Simple example: 
        -When you write printf("Hello"); in C, the compiler translates that exact 
        line into native CPU instructions before the program ever runs. When you 
        launch the executable, your computer runs those instructions directly on 
        the hardware at maximum speed.

2. Java: The Hybrid Approach (Bytecode + JVM)

    How it works: 
        -Java uses a two-step process. First, the Java compiler translates your source 
        code into an intermediate format called bytecode. Then, the Java Virtual Machine
        (JVM) executes that bytecode, often translating hot sections of it into native 
        machine code on-the-fly using Just-In-Time (JIT) compilation.

    Simple example: 
        -Your System.out.println("Hello"); becomes a standardized Java bytecode 
        instruction. The JVM on your specific computer reads that bytecode and converts 
        it into native instructions for your specific CPU. This allows the same compiled 
        file to run on Windows, Mac, or Linux ("write once, run anywhere") as long as the 
        JVM is installed.

3. Python: Dynamic Interpretation

    How it works: 
        -Python is traditionally an interpreted language. Under the hood, 
        Python compiles source code into a hidden intermediate bytecode 
        (.pyc files) the first time it runs, which is then fed into the Python Virtual 
        Machine (PVM) to be executed line-by-line at runtime.

    Simple example: 
        -When you run print("Hello"), the Python interpreter reads the script, 
        translates it, and the PVM evaluates and executes the instruction on the fly. 
        Because this translation happens dynamically while the program runs—and because 
        Python's dynamic typing requires extra type-checking checks at runtime—Python is 
        generally much more flexible, but significantly slower than C or Java.

Summary ComparisonC: 
    
    -Source Code $\rightarrow$ Compiler $\rightarrow$ Native Machine Code $\rightarrow$ 
     CPU (Fastest, platform-specific)
    -Java: Source Code $\rightarrow$ Compiler $\rightarrow$ Bytecode $\rightarrow$ JVM 
     (JIT) $\rightarrow$ CPU (Portable, balanced speed)
    -Python: Source Code $\rightarrow$ Interpreter/PVM $\rightarrow$ CPU 
     (Most flexible, slower execution)
"""