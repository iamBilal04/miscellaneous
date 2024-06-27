import pymysql

def create_connection():
    return pymysql.connect(
        user="root",
        password="Fouzan$08",
        host="host.docker.internal",
        database="test"
    )


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS book(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), 
        cover VARCHAR(255))""")


def add_book(connection, book, cover):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book (title, cover) VALUES (%s, %s)", (book, cover))
    connection.commit()
    cursor.close()


def fetch_all_books(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT title FROM test.book")
    books = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return books


def main():
    connection = create_connection()
    if connection:
        print("SUCSEC")
        create_table(connection)
    else:
        print("Bonka")

    while True:
        print("1. Add book")
        print("2. Show all book")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book = input("Enter the book name: ")
            cover = input("Enter cover: ")
            books=add_book(connection, book, cover)
            print(f"The book: {books} was added to list")

        elif choice == '2':
            books = fetch_all_books(connection)
            if books:
                print(f"The books are:")
                for book in books:
                    print(f"Name: {book}")

            else:
                print("No books there")
        elif choice == '3':
            print("Bye")
            break
        else:
            print("Enter valid things")

    connection.close()


if __name__ == "__main__":
    main()
