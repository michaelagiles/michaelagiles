# Cafeteria Problem Solver

These functions were provided to solve a problem set in a python course. The
aim is to think about how stacks and queues work.

## The Cafeteria Problem

The problem was set as follows:

> **Objective:** The school cafeteria serves brown (0) and white (1) bread
toasted sandwiches to students. Students queue to get their preferred bread
from the sandwiches kept in a stack. If the student at the front of the queue
prefers the type of sandwich that is on top of the sandwich stack, they take
the sandwich and leave the queue. Otherwise, they pass on the sandwich and move
to the end of the queue. This continues until none of the queue students want
to take the top sandwich and are thus unable to eat. Return the number of
students that are unable to eat.

## How to Use the Solver

The functions used for solving this problem are contained in the file
`cafeteria_queue.py`. There is the main solver function `sandwich_problem` and
another function, `queue_constructor` that offers a user-friendly way of
constructing the queues for use in `sandwich_problem`.

### `sandwich_problem(students, sandwiches, details=False)`

This function will take in the student queue and the sandwich stack and return
the number of students that are left unable to eat.

The students argument must be a list of 0s (representing a preference for brown
bread) and 1s (for white bread preference) only. The sandwiches argument
similarly must be a list of 0s and 1s only. The **last** entry in the relevant
list represents the front of the student queue or the top of the sandwich
sack. `queue_constructor()` will handle this.

The function prints the number of students that are left without a sandwich.
The optional `details` argument will print extra information after solving the
sandwich problem if it has any truthy value. Where relevant this will include:

- Preferences of any students left over.
- Bread type of any sandwiches left over.
- The number of passes.

### `queue_constructor()`

This function takes no arguments and has the user answer several questions to
generate a list for `sandwich_problem`. If the user selects that they do not
care about the order of the sandwiches/student preferences, the brown bread
will be at the front of the queue/top of the stack.

`queue_constructor` offers the choice of whether or not to manually order the
sandwiches/preferences. The order does affect the solution of the problem as
it is significant that the sandwiches are arranged in a stack such that only
the top sandwich is available to take. The student order will only affect the
number of passes (viewable using the details flag of `sandwich_problem`). This
can be seen in the sample outputs below.

Consequently, one way to set up and solve the problem would be as follows:

```
student_queue = queue_constructor()
sandwich_stack = queue_constructor()
hungry_students = sandwich_problem(student_queue, sandwich_stack)
```

The number of students left without sandwiches would be stored in 
`hungry_students`.

## Sample Outputs

### Without Details Flag

#### Five of each sandwich, five of each preference
Input:
```
student_queue = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
sandwich_stack = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
hungry_students = sandwich_problem(student_queue, sandwich_stack)
print(hungry_students)
```

Output:

```
All of the students received their preferred sandwiches.
0
```

#### Five of each sandwich, seven students prefer brown, three prefer white
Input:
```
student_queue = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
sandwich_stack = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
hungry_students = sandwich_problem(student_queue, sandwich_stack)
print(hungry_students)
```

Output:
```
The number of students left unable to eat is: 4
4
```
Note that this is a part of the problem as posed; there were enough sandwiches
for each student if the sandwiches were not arranged in a stack. In this
example, a white sandwich is at the top of the stack with brown sandwiches
below it when there are four students who prefer brown bread but none who
prefer white left in the queue. 

### With Details Flag

#### Five of each sandwich, five of each preference

Input:
```
student_queue = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
sandwich_stack = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
hungry_students = sandwich_problem(student_queue, sandwich_stack, True)
print(hungry_students)
```

Output:

```
All of the students received their preferred sandwiches.
White sandwiches left over: 0
Brown sandwiches left over: 0
The number of times a student rejected a sandwich: 20
0
```

#### Five of each sandwich, seven students prefer brown, three prefer white
Input:
```
student_queue = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
sandwich_stack = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
hungry_students = sandwich_problem(student_queue, sandwich_stack, True)
print(hungry_students)
```

Output:
```
The number of students left unable to eat is: 4
Number of students preferring white bread: 0
Number of students perferring brown bread: 4
White sandwiches left over: 2
Brown sandwiches left over: 2
The number of times a student rejected a sandwich: 18
4
```

#### Five of each sandwich, seven students prefer brown, three prefer white, brown sandwiches on top of the stack
Input:
```
student_queue = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
sandwich_stack = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
hungry_students = sandwich_problem(student_queue, sandwich_stack, True)
print(hungry_students)
```

Output:
```
The number of students left unable to eat is: 2
Number of students preferring white bread: 0
Number of students perferring brown bread: 2
White sandwiches left over: 2
Brown sandwiches left over: 0
The number of times a student rejected a sandwich: 7
2
```
