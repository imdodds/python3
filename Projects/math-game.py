questions = [
  [31, 87],
  [51, 23],
  [12, 29],
  [42, 81],
  [78, 31],
  [61, 59],
  [11, 13],
  [42, 12],
  [23, 29],
  [31, 51],
]

score = 0

for a, b in questions:
    answer = input(f"What is {a} + {b}? ")
    if int(answer) == a + b:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {a + b}")

if score > len(questions) / 2:
  print(f"Great job! You got {score} out of {len(questions)} correct")
else:
  print(f"Try again! You got {score} out of {len(questions)} correct")