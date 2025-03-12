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
            return jsonify(std)
        print(std)
    return jsonify('not found')


if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )