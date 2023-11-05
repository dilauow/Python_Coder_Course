def get_passing_students():
  """Returns a new list that contains only the scores of the students who passed the test.


  Returns:
    A new list that contains only the scores of the students who passed the test.
  """
  student_Scores = []
  while True:
      score = int(input("Enter the student's score: "))
      student_Scores.append(score)
      if input("Do you want to add another student score? (y/n)") != "y":
          break

  passing_students_Score = []
  for score in student_Scores:
    if score >= 60:
      passing_students_Score.append(score)
  return passing_students_Score


# Get a list of students and their scores from the user.


# Get the list of passing students.
passing_students = get_passing_students()
