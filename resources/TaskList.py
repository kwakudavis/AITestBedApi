from flask_restful import Resource



class TaskList(Resource):
    """
    Documentation for TaskList Resource: the TaskList resource interacts with any request to interact with all existing Tasks for within a particular training instance.

    More details.
    """

    def get(self,model_number):
        return {"message":"Returns all the available in a training instance"}

    def delete(self,model_number):
        return {"message":"Deletes all the lists available in a training instance"}
