#Patient Triage & Emergency Room Queue Management -First-In-First-Out (FIFO) for fair patient processing
# Using deque for efficient queue operations
from collections import deque

# ER Patient Queue (Critical → Stable)
er_queue = deque()

# Patients arrive (critical cases jump queue)
er_queue.append("Broken Arm")        # Stable case
er_queue.append("Severe Burn")       # Critical case
er_queue.appendleft("Heart Attack")  # MOST critical
er_queue.append("Flu")              # Stable case
er_queue.append("Shortness of Breath")  # Critical case

print("ER Queue:", list(er_queue))  
# Output: ['Heart Attack', 'Broken Arm', 'Severe Burn']

# Process patients
while er_queue:
    current = er_queue.popleft()
    print(f"Treating: {current} → Remaining: {list(er_queue)}")