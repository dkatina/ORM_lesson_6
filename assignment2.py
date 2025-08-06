from sqlalchemy import create_engine, Integer, String, DateTime,Float, ForeignKey, Table, Column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from datetime import datetime, timezone

Base = declarative_base() #Will be inherited by all model classes, so they can behave as tables

engine = create_engine('sqlite:///book_club.db')


class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    author: Mapped[str] = mapped_column(String(120), nullable=False)
    
    reviews: Mapped[list['Reviews']] = relationship('Reviews', back_populates='book')
    readers: Mapped[list['Readers']] = relationship('Readers', secondary='reviews', back_populates='books')

class Readers(Base):
    __tablename__ = "readers" 

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(360), nullable=False, unique=True)

    reviews: Mapped[list['Reviews']] = relationship("Reviews", back_populates='reader')
    books: Mapped[list['Books']] = relationship("Books", secondary='reviews', back_populates='readers')


class Reviews(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id: Mapped[int] = mapped_column(Integer, ForeignKey('readers.id'), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    book: Mapped['Books'] = relationship('Books', back_populates='reviews')
    reader: Mapped['Readers'] = relationship('Readers', back_populates='reviews')

Base.metadata.create_all(bind=engine)



book_1 = Books(title='Something', author='someone')
book_2 = Books(title='Something2', author='someone')
book_3 = Books(title='Something3', author='someone')

session.add_all([book_1, book_2, book_3]) #Allows you to add multiple instances to you db session at one time.
session.commit()