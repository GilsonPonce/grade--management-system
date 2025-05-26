# pylint: disable=missing-docstring, invalid-name
class Student:
    """
    Representa a un estudiante con su ID, nombre y calificaciones.
    """
    def __init__(self, student_id, name):
        # PEP8: Evitar variables de un solo carácter como 's', usar 'self'
        self.student_id = student_id
        self.name = name
        self.grades = []  # Renombrado a 'grades' para mayor claridad
        self.is_passed = False  # Usar tipo bool en lugar de string
        self.honor = False  # Tipo bool, no '?'

    def add_grade(self, grade):
        # PEP8: Nombrar métodos en snake_case
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Warning: Grade {grade} is not a number and was ignored.")

    def calc_average(self):
        # Evitar división por cero
        if not self.grades:
            return 0.0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        # Llamar correctamente a calc_average y comparar
        if self.calc_average() > 90:
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, index):
        # Manejar excepciones para índices inválidos
        try:
            del self.grades[index]
        except IndexError:
            print(f"Warning: Index {index} is out of range. No grade deleted.")

    def report(self):
        # Mejorar formato y corregir errores de tipo
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calc_average():.2f}")
        print(f"Passed: {'Yes' if self.calc_average() >= 60 else 'No'}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")

def startrun():
    # Creación de instancia con datos válidos
    a = Student("001", "Alice")
    a.add_grade(100)
    a.add_grade(50)  # Cambiado a número
    a.add_grade(75)
    a.calc_average()  # Aunque ya se usa en report
    a.check_honor()
    a.delete_grade(5)  # Esto imprimirá un warning
    a.report()

if __name__ == "__main__":
    startrun()
