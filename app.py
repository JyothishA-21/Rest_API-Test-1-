from flask import Flask , jsonify

todo = Flask(__name__)

students=[
    {
        "id":1,
        "name":"Nani",
        "age":20
    },
    {
        "id": 2,
        "name": "Chinnu",
        "age": 25
    },
    {
        "id": 3,
        "name": "Rahul",
        "age": 10
    }
]
@todo.route('/students-list')
def get_student_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            print(std)
            return jsonify(std)


if __name__ == '__main__':
    todo.run(
        debug=True
    )