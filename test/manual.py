import sys
sys.path.append('..')
from src.fileio.reader import create_vertex_list
import io

test_stream = io.StringIO()

def create_vertex_no_arrow():
    test_stream.write("A (B, 2), (C, 7), (D, 8)")
    test_stream.seek(0)
    print(str(test_stream))
    result = create_vertex_list(test_stream)
    print(result)

def create_vertex_arrow():
    test_stream.write("A -> ")
    result = create_vertex_list(test_stream)

def create_vertex_extra_data():
    test_stream.write("A -> (B, 2, 4)")
    result = create_vertex_list(test_stream)

def create_vertex_non_number():
    test_stream.write("A -> (B, p)")
    result = create_vertex_list(test_stream)

if __name__ == "__main__":
    create_vertex_arrow()
    create_vertex_no_arrow()
    create_vertex_extra_data()
    create_vertex_non_number()