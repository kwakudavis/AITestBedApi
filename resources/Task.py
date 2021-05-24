from flask_restful import Resource



class Task(Resource):
    """
    Documentation for Task Resource: the Task resource interacts with any request to interact with an existing Task or create a new Image processing Task.

    More details.
    """

    def post(self,id):
        return {"message": "A task has been added succesfully for processing task with id: "+id},201


    def get(self,id):
        return {"message": "Gets an existing Task"}


    def put(self,id):
        return {"message": "Updates an existing Task"}


    def delete(self,id):
        return {"message": "Deletes an existing Task"}
