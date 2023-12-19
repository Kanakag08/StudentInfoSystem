from util.DBConnection import DBConnection

# Example usage
def createTable():
    conn=None
    try:
            conn,stmt=DBConnection.open()
            if conn:
                stmt.execute('''create table if not exists Course(course_id int primary key,
                                course_name varchar(20), course_code varchar(30), instructor_name varchar(50)) ''')
                print("Database initialized successfully.")

    except Exception as e:
        print(f"Error during database initialization: {e}")

    finally:
        if conn:
            DBConnection.close(conn)