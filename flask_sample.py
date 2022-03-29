from flask import Flask,jsonify


courses=[{'courseId':0,'c_name':'python','desc':'python is a high level language'}
,{'courseId':1,'c_name':'java','desc':'java is a Programmable language'}
,{'courseId':2,'c_name':'JS','desc':'JS is a client side langfugae'},
{'courseId':3,'c_name':'TS','desc':'TS is a Static supported JS language'},
{'courseId':4,'c_name':'mongoDB','desc':'mongo is a block DB'}]


app=Flask(__name__)


@app.route('/')
def index():
    return f"Hello World"

@app.route('/courses/',methods=['GET'])
def get_courses():
    return jsonify({'Courses':courses})

@app.route('/courses/<int:courseId>/',methods=['GET'])
def get_courses_by_id(courseId):
    return jsonify({'Courses':courses[courseId]})

@app.route('/courses/',methods=['POST'])
def submit_courses():
    course={'courseId':5,'c_name':'MySQL','desc':'MySQL'}
    courses.append(course)
    return jsonify({'Updated Courses':course})

@app.route('/courses/<int:courseId>/',methods=['PUT'])
def update(courseId):
    courses[courseId]['desc']="xyz"
    return jsonify({'Updated Course is':courses[courseId]})

@app.route('/courses/<int:courseId>/',methods=['DELETE'])
def delete_courses(courseId):
    courses.remove(courses[courseId])
    return jsonify({"Deleted Courses":True})


if __name__=='__main__':
    app.run(debug=True)