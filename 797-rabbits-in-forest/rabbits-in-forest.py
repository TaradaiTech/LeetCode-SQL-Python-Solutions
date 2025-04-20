class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        
        # Count how many rabbits gave each answer
        answer_frequency = Counter(answers)
        total_rabbits = 0

        for answer, count in answer_frequency.items():
            group_size = answer + 1  # Each rabbit says there are 'answer' others of the same color
            groups_needed = (count + answer) // group_size  # Round up: fill full groups
            total_rabbits += groups_needed * group_size  # Each group contributes full size

        return total_rabbits