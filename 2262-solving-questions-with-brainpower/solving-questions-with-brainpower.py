class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Get the total number of questions
        num_questions = len(questions)
        # Create an array to store the maximum points we can earn starting from each question
        max_points = [0] * num_questions
        # Initialize the 'prev_max_points' variable with the points of the last question
        prev_max_points = questions[-1][0]
        # Traverse the questions in reverse order (starting from the last question)
        for current_question_index in range(num_questions - 1, -1, -1):
            # Set the initial value of 'max_points[current_question_index]' as 'prev_max_points'
            max_points[current_question_index] = prev_max_points
            # Extract the points (question_points) and the brainpower required (brainpower_cost) for the current question
            question_points, brainpower_cost = questions[current_question_index]
            # Calculate the index of the next question that can be solved after skipping 'brainpower_cost' questions
            next_question_index = current_question_index + brainpower_cost + 1
            # If the next solvable question exists (i.e., next_question_index < num_questions), add the points from that question
            if next_question_index < num_questions:
                question_points += max_points[next_question_index]
            # If solving this question gives more points than the previous maximum, update 'max_points[current_question_index]'
            if question_points > prev_max_points:
                max_points[current_question_index] = question_points
            # Update 'prev_max_points' to the maximum points that can be earned starting from the current question
            prev_max_points = max_points[current_question_index]
        # Return the maximum points we can earn starting from the first question
        return max_points[0]
