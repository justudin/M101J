#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from pymongo import Connection
 
connection = Connection("localhost", 27017)
db = connection["school"]
collection = db["students"]
for student in collection.find({"scores.type": "homework"}):
    homeworkscore = []
    for score in student['scores']:
        if score["type"] == "homework":
            homeworkscore.append(score["score"])
    db.students.update({"_id": student["_id"]}, {"$pull": {"scores": {"score": min(homeworkscore)}}})
