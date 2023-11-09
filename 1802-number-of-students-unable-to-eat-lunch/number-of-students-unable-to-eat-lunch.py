class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        square_students = sum(students)
        circular_students = len(students) - square_students

        for sandwiche in sandwiches:
            if sandwiche :
                if square_students: square_students -= 1
                else: return circular_students
            else:
                if circular_students: circular_students-=1
                else: return square_students
        return 0
            

        