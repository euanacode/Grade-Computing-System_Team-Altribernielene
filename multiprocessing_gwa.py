from multiprocessing import Process, Queue
import time

def compute_gwa_mp(subject_name, grade, index, result_queue):
    """
    Compute GWA for a single subject grade.
    Sends result to queue for safe inter-process communication.
    """
    # Simulate some processing time
    time.sleep(0.01)
    
    # Send result to queue
    result = {
        'index': index,
        'subject': subject_name,
        'grade': grade,
        'process_id': f"P{index+1}"
    }
    result_queue.put(result)
    print(f"[Process-P{index+1}] Subject: {subject_name}, Grade: {grade}")

def main():
    print("=" * 60)
    print("GRADE COMPUTING SYSTEM - MULTIPROCESSING VERSION")
    print("=" * 60)
    
    # Get number of subjects
    while True:
        try:
            num_subjects = int(input("\nEnter number of subjects: "))
            if num_subjects > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get grades for each subject
    grades_list = []
    subjects = []
    
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        while True:
            try:
                grade = float(input(f"Enter grade for {subject}: "))
                if 0 <= grade <= 100:
                    subjects.append(subject)
                    grades_list.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Create a queue for results
    result_queue = Queue()
    
    # Start timing
    start_time = time.time()
    
    # Create and start processes
    processes = []
    print("\n--- Starting Processes ---")
    
    for i, (subject, grade) in enumerate(zip(subjects, grades_list)):
        p = Process(
            target=compute_gwa_mp,
            args=(subject, grade, i, result_queue)
        )
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    # End timing
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Collect results from queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    # Calculate overall GWA
    overall_gwa = sum(grades_list) / len(grades_list)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"\nTotal Subjects: {num_subjects}")
    print(f"Overall GWA: {overall_gwa:.2f}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print("\nDetailed Results:")
    
    # Sort results by original index for consistent display
    sorted_results = sorted(results, key=lambda x: x['index'])
    for result in sorted_results:
        print(f"  {result['subject']}: {result['grade']} (processed by {result['process_id']})")
    
    print("=" * 60)
    
    return execution_time, overall_gwa

if __name__ == "__main__":
    main()
