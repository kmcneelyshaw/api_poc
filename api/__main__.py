from bson import ObjectId
from pymongo import MongoClient
import hug


client = MongoClient("db", 27017)
db = client["social-media"]
comments = db["comments"]

@hug.get("/comments", output=hug.output_format.pretty_json)
def show_comments():
    """Returns a list of comments currently in the database"""
    items = list(comments.find())
    # JSON conversion chokes on the _id objects, so we convert
    # them to strings here
    for i in items:
        i["_id"] = str(i["_id"])
    return items

@hug.post("/comments", status_code=hug.falcon.HTTP_201)
def create_comment(content: hug.types.text):
    """Inserts the given comment as a new item in the database. Returns the ID of the newly created item."""
    comment = {"content": content, "likes": 0}
    comments.insert_one(comment)
    return str(comment["_id"])

@hug.get("/comments/{id}", output=hug.output_format.pretty_json)
def show_comment(id: str):
    """Returns the comment with the specified id"""
    comment = comments.find_one({"_id": ObjectId(id)})
    # JSON conversion chokes on the _id objects, so we convert
    # them to strings here
    comment["_id"] = str(comment["_id"])
    return comment

@hug.delete("/comments/{id}")
def delete(id: str):
    """Deletes the comment with the specified id"""
    comments.delete_one({"_id": ObjectId(id)})

@hug.put("/comments/{id}/upvote")
def upvote(id: str):
    """Increments the likes on the comment with the specified id"""
    # TODO: Better error handling when the document doesn't exist
    # (py)mongo documentation is proving remarkably difficult at
    # showing how to handle this gracefully.  Currently if the id is
    # not found, return 500 and cry.
    comments.update_one({"_id": ObjectId(id)}, {"$inc": {"likes": 1}})


@hug.put("/comments/{id}/downvote")
def downvote(id: str):
    """Decrements the likes on the comment with the specified id"""
    # TODO: Better error handling when the document doesn't exist
    # (py)mongo documentation is proving remarkably difficult at
    # showing how to handle this gracefully.  Currently if the id is
    # not found, return 500 and cry.
    comments.update_one({"_id": ObjectId(id)}, {"$inc": {"likes": -1}})
