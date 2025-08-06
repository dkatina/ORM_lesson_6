from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from datetime import datetime

Base = declarative_base() #Will be inherited by all model classes, so they can behave as tables

engine = create_engine('sqlite:///school.db')


student_course = Table(
    "student_course",
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

student_club = Table(
    "student_club",
    Base.metadata,
    Column("student_id", Integer, ForeignKey('students.id')),
    Column("club_id", Integer, ForeignKey("clubs.id"))
)


class Students(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    parent_email: Mapped[str] = mapped_column(String(360), nullable=False)

    courses: Mapped[list['Courses']] = relationship('Courses', secondary=student_course, back_populates='students' )
    clubs: Mapped[list['Clubs']] = relationship('Clubs', secondary=student_club, back_populates='students')


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    instructor: Mapped[str] = mapped_column(String(200))

    students: Mapped[list['Students']] = relationship('Students', secondary=student_course, back_populates='courses')

class Clubs(Base):
    __tablename__ = 'clubs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(String(360), nullable=False)

    students: Mapped[list['Students']] = relationship('Students', secondary=student_club, back_populates='clubs')


Base.metadata.create_all(bind=engine)


