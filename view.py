from tkinter import *


class gui:
    def __init__(self,window):
        self.window = window

        # Prompts for user input of student numbers

        self.frame_numStudents = Frame(self.window)
        self.label_numStudents = Label(self.frame_numStudents, text='Number of Students:')
        self.entry_numStudents = Entry(self.frame_numStudents)

        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='right')
        self.frame_age.pack(anchor='w', pady=10)

        #Prompts for student grades - number of grades must match number of students

        self.frame_grades = Frame(self.window)
        self.label_grades = Label(self.frame_grades, text='Students\' grades:')
        self.entry_grades = Entry(self.frame_grades)

        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='right')
        self.frame_age.pack(anchor='w', pady=10)

        #Output for Students and Score

        self.frame_output - Frame(self.window)
        self.label_output = Label(self.frame_output, text='Results:')
        self.label_output.pack(anchor='w', pady=10)

        # Submit

        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.window, text='Save', command=self.clicked)

        self.button_submit.pack()
        self.frame_submit.pack(pady=10)

        #error?
        self.frame_error = Frame(self.window)


    def clicked(self):

        # When called, creates the var num_students and the list grades_list
        num_students = self.entry_numStudents.get()
        self.entry_numStudents.delete(0, END)

        student_grades = []
        grades_list = self.entry_grades.get()

        for i in grades_list:
            student_grades.append(i)

        self.entry_grades.delete(0, END)

        while len(grades_list) < num_students:
            self.label_error = Label(self.frame_output, text='Enter a number of grades equal to the number of students.')
            self.label_error.pack()
            self.frame_error.pack()

        best_score = max(grades_list)
        x = 0

        while x < len(grades_list):
            self.frame_final = Frame(self.window)
            self.label_final = Label(self.frame_final, text=f'Student {x + 1}s score is {grades_list[x]} and their grade is {grade_scale(grades_list[x], best_score)}')
            x += 1

        def grade_scale(score, best_score):
            if score >= best_score - 10:
                return 'A'
            elif score >= best_score - 20:
                return 'B'
            elif score >= best_score - 30:
                return 'C'
            elif score >= best_score - 40:
                return 'D'
            else:
                return 'F'






