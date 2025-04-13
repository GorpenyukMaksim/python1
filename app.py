from flask import Flask, render_template
from models import Artist, Album, Song, Book, Movie, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_preferences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)

@app.route('/books')
def books():
    books_list = Book.query.all()
    return render_template('books.html', books=books_list)

@app.route('/movies')
def movies():
    movies_list = Movie.query.all()
    return render_template('movies.html', movies=movies_list)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Добавляем музыкальных исполнителей
        artist1 = Artist(name='Radiohead')
        artist2 = Artist(name='Hans Zimmer')
        artist3 = Artist(name='Daft Punk')
        artist4 = Artist(name='Pink Floyd')
        db.session.add_all([artist1, artist2, artist3, artist4])
        db.session.commit()

        # Добавляем музыкальные альбомы
        album1 = Album(title='OK Computer', year='1997', artist=artist1)
        album2 = Album(title='In Rainbows', year='2007', artist=artist1)
        album3 = Album(title='Interstellar OST', year='2014', artist=artist2)
        album4 = Album(title='Random Access Memories', year='2013', artist=artist3)
        album5 = Album(title='The Dark Side of the Moon', year='1973', artist=artist4)

        # Добавляем песни
        song1 = Song(title='Paranoid Android', length='6:23', track_number=3, album=album1)
        song2 = Song(title='Weird Fishes', length='5:18', track_number=5, album=album2)
        song3 = Song(title='Cornfield Chase', length='2:06', track_number=4, album=album3)
        song4 = Song(title='Get Lucky', length='6:09', track_number=5, album=album4)
        song5 = Song(title='Time', length='6:53', track_number=4, album=album5)

        # Добавляем книги
        book1 = Book(title='1984', author='George Orwell', year=1949, genre='Dystopian')
        book2 = Book(title='The Lord of the Rings', author='J.R.R. Tolkien', year=1954, genre='Fantasy')
        book3 = Book(title='Dune', author='Frank Herbert', year=1965, genre='Sci-Fi')

        # Добавляем фильмы
        movie1 = Movie(title='The Shawshank Redemption', director='Frank Darabont', year=1994, genre='Drama')
        movie2 = Movie(title='Inception', director='Christopher Nolan', year=2010, genre='Sci-Fi')
        movie3 = Movie(title='Pulp Fiction', director='Quentin Tarantino', year=1994, genre='Crime')

        db.session.add_all([
            album1, album2, album3, album4, album5,
            song1, song2, song3, song4, song5,
            book1, book2, book3,
            movie1, movie2, movie3
        ])
        db.session.commit()

