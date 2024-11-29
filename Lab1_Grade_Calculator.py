# Step 1: Ask the user for test scores and store them in a list

scores = input("Enter test scores separated by spaces: ").split()
scores = [float(score) for score in scores]  # Convert strings to floats

# Step 2: Calculate the average score
average_score = sum(scores) / len(scores)

# Step 3: Determine the letter grade
if 90 <= average_score <= 100:
    grade = "A"
elif 80 <= average_score < 90:
    grade = "B"
elif 70 <= average_score < 80:
    grade = "C"
elif 60 <= average_score < 70:
    grade = "D"
else:
    grade = "F"

# Step 4: Print the average score and letter grade
print(f"Average score: {average_score:.2f}")
print(f"Letter grade: {grade}")
