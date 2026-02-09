Exploring Multithreading and Multiprocessing in Python

Lab Overview
- This laboratory explores the differences between multithreading and multiprocessing in Python through a Grade Computing System that calculates General Weighted Average (GWA).

Group Members:
Bautista, Chrisa Lene Joy
Beatisula, Nathaniel
Calo, Liberty Case
Luna, Alyssa Euana
Pabonita, Trisha Aira

Execution Results:
Sample Test with 4 Grades
Method          - Execution Order - GWA Output - Execution Time
Multithreading  - May vary        - 86.25      - ~0.015 seconds
Multiprocessing - May vary        - 86.25      - ~0.045 seconds
Note: Actual execution times may vary based on system specifications.

Answers to Lab Questions:
1. Which approach demonstrates true parallelism in Python? Explain.
- Multiprocessing demonstrates true parallelism in Python.
Explanation:
- Multiprocessing creates separate python processes, each with its own python interpreter and memory space. Each process runs on a separate CPU core, allowing true simultaneous execution of code.
- Multithreading in Python does not achieve true parallelism for CPU bound tasks due to the Global Interpreter Lock (GIL). The GIL is a mutex that protects access to python objects, preventing multiple threads from executing python bytecode. With multiprocessing also, each process has its own GIL, so they can execute Python code truly in parallel across multiple CPU cores.

2. Compare execution times between multithreading and multiprocessing.
Answer:
For Small Tasks (4-10 grades):
- Multithreading is faster (~0.010-0.020 seconds)
- Multiprocessing is slower (~0.040-0.080 seconds)
= Multiprocessing has significant overhead from creating separate processes

For Medium Tasks (100 grades):
- Multithreading: ~0.020-0.050 seconds
- Multiprocessing: ~0.100-0.200 seconds
= Overhead still dominates for simple calculations

For Large Tasks (1000 grades):
- Multithreading: ~0.100-0.200 seconds
- Multiprocessing: ~0.500-1.000 seconds
= For simple arithmetic, thread overhead is minimal; process overhead is substantial

3. Can Python handle true parallelism using threads? Why or why not?
- No, Python cannot handle true parallelism using threads for CPU bound tasks.
Explanation:
The Global Interpreter Lock (GIL):
- Python has a Global Interpreter Lock (GIL) in the CPython implementation
- The GIL is a mutex that allows only one thread to execute Python bytecode at a time
- Even on multi-core systems, only one thread can execute Python code at any given moment

Why the GIL Exists:
- Memory management: Python uses reference counting for memory management
- The GIL simplifies the implementation and makes it thread safe
- It prevents race conditions when modifying Python objects

Exception - I/O-bound tasks:
- Threads can achieve concurrency (not parallelism) for I/O-bound operations
- When a thread is waiting for I/O (file reading, network requests), it releases the GIL
- Other threads can execute while one is waiting for I/O
- This makes threading useful for I/O-bound tasks, even without true parallelism

Alternatives:
- Use multiprocessing for CPU bound tasks (true parallelism)
- Use asyncio for I/O-bound tasks (efficient concurrency)
- Use threading for I/O-bound tasks with blocking operations

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?
Answer:
For our simple GWA calculation, multithreading is still faster.
Results with 1000 grades:
- Multithreading: ~0.100-0.200 seconds
- Multiprocessing: ~0.500-1.500 seconds

Why Multithreading is Faster:
* Process Creation Overhead:
  - Creating 1000 separate processes requires significant system resources
  - Each process needs its own memory space, Python interpreter, and system resources
  - Process creation and teardown takes substantial time

* Inter-Process Communication (IPC):
  - Processes cannot share memory directly
  - Data must be serialized/deserialized when passing between processes
  - Queue operations add overhead

* Task Simplicity:
  - Our GWA calculation is computationally trivial (just addition and division)
  - The calculation time is microseconds per grade
  - The overhead of creating processes far exceeds the computation time

* Thread Efficiency:
  - Threads share the same memory space (minimal overhead)
  - Thread creation is lightweight
  - Context switching between threads is fast

When Multiprocessing Would Win:
- If each grade required complex CPU-intensive calculations (e.g., statistical analysis, encryption, image processing)
- If each task took milliseconds to seconds to complete
- When the computation time greatly exceeds the process creation overhead
- With fewer, larger tasks (4-8 processes handling 250 grades each)

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
- CPU-Bound Tasks → Use MULTIPROCESSING
Definition: Tasks that spend most of their time doing computations (using the CPU)
Examples:
- Mathematical calculations (matrix operations, statistics)
- Data processing and transformation
- Image/video processing
- Encryption/decryption
- Machine learning model training
- Scientific simulations

Why Multiprocessing:
- Bypasses the GIL by using separate processes
- Achieves true parallelism across multiple CPU cores
- Each process can fully utilize a CPU core
- Scales with the number of available CPU cores

Example Use Case:
# Processing large dataset - CPU intensive
from multiprocessing import Pool
def process_data(data_chunk):
    # Complex mathematical operations
    return expensive_calculation(data_chunk)
with Pool(processes=4) as pool:
    results = pool.map(process_data, data_chunks)

- I/O-Bound Tasks → Use MULTITHREADING or ASYNCIO
Definition: Tasks that spend most of their time waiting for input/output operations
Examples:
- File reading/writing
- Network requests (API calls, web scraping)
- Database queries
- User input
- Downloading files

Why Multithreading:
- When one thread waits for I/O, it releases the GIL
- Other threads can execute during the wait time
- Lower overhead than multiprocessing
- Shared memory makes data sharing easy

Why Asyncio (Better Alternative):
- More efficient than threading for I/O-bound tasks
- Single-threaded cooperative multitasking
- Lower memory overhead
- Better scalability for many concurrent I/O operations

Example Use Case:
# Making multiple API requests - I/O intensive
import threading
import requests
def fetch_url(url):
    response = requests.get(url)  # I/O wait - releases GIL
    return response.json()
threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

6. How did your group apply creative coding or algorithmic solutions in this lab?
- Our group implemented several creative solutions to enhance the grade
computing system:
* Thread-Safe Result Collection
  - Used threading.Lock() to safely append results to a shared list
  - Prevented race conditions when multiple threads write simultaneously
  - Demonstrated proper concurrent programming practices
* Inter-Process Communication with Queues
  - Implemented Queue for safe data passing between processes
  - Each process sends results to a shared queue
  - Main process collects and sorts results after all processes complete
* Input Validation System
  - Created robust error handling for user inputs
  - Validates that grades are between 0-100
  - Handles non-numeric inputs gracefully
  - Ensures positive number of subjects
* Execution Order Tracking
  - Assigned index numbers to track which thread/process handled each grade
  - Sorted results by original index for consistent display
  - Demonstrated that execution order varies between runs
* Performance Measurement
  - Implemented precise timing using time.time()
  - Created comparison script to test multiple input sizes
  - Automated testing with 4, 10, 100, and 1000 grades
* User-Friendly Interface
  - Clear formatted output with section dividers
  - Shows which thread/process handled each subject
  - Displays overall GWA and execution time
  - Named threads/processes for easy identification
7. Scalability Testing
  - Designed code to handle variable input sizes
  - Tested performance characteristics across different workloads
  - Provided insights on when to use each approach
8. Code Organization
  - Separated concerns (calculation, display, timing)
  - Created reusable functions
  - Maintained clean, readable code structure
  - Added comprehensive comments
