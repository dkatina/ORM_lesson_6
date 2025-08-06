from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker
from datetime import datetime, timezone

Base = declarative_base() #Will be inherited by all model classes, so they can behave as tables

engine = create_engine('sqlite:///school2.db')




student_club = Table( #Association Table Object
    "student_club",
    Base.metadata,
    Column("student_id", Integer, ForeignKey('students.id')),
    Column("club_id", Integer, ForeignKey("clubs.id"))
)


class Students(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True) #When instantiating, don't need info for the id, as it auto-increments
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    parent_email: Mapped[str] = mapped_column(String(360), nullable=False)

   
    clubs: Mapped[list['Clubs']] = relationship('Clubs', secondary=student_club, back_populates='students')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='student')
    courses: Mapped[list['Courses']] = relationship('Courses', secondary='enrollments', back_populates='students')


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    instructor: Mapped[str] = mapped_column(String(200))

    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='course')
    students: Mapped[list['Students']] = relationship('Students', secondary='enrollments', back_populates='courses')

class Enrollments(Base): #Association Model
    __tablename__ = 'enrollments'

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'))
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("courses.id"))
    enrollment: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    notes: Mapped[str] =mapped_column(String(500))
    grade: Mapped[str] =mapped_column(String(2))

    student: Mapped['Students'] =relationship('Students', back_populates='enrollments')
    course: Mapped['Courses'] =relationship('Courses', back_populates='enrollments')

    

class Clubs(Base):
    __tablename__ = 'clubs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(String(360), nullable=False)

    students: Mapped[list['Students']] = relationship('Students', secondary=student_club, back_populates='clubs')


Session = sessionmaker(bind=engine) #Creating a session class
session = Session() #Creating and instance f session

#Creating a student USING our Students model
# alice = Students(first_name='Alice', last_name='Wonderland', parent_email='madhatter@email.com')
# session.add(alice) #adding the new student object to my database session
# session.commit() #Finalizing adding the new student to the database, by committing the session

#Creating a new Course USING our Courses model
# history = Courses(title='History', instructor='Dr. Barnett')
# session.add(history)
# session.commit()

#Enrolling Alice into History
# new_enrollment = Enrollments(student_id=1, course_id=1, notes='Just beginning course.', grade='A')
# session.add(new_enrollment)
# session.commit()




student = session.get(Students, 1) # == SELECT * FROM students WHERER id = 1
print('\n\n\n----------------- Alice--------------------------')
print(student) #student is a Students object
print(student.first_name)
print(student.last_name)
print(student.parent_email)

print(student.courses[0].title)









Base.metadata.create_all(bind=engine)

