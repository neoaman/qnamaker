from pymongo import MongoClient
from icecream import ic

import logging
import sys

logger = logging.getLogger("qnamaker")

conn = MongoClient("mongodb+srv://neoaman:n30m0ng0passw0rd@oneo.easy3.mongodb.net/test")
db,collection = "qna","gcp_mle"
table = conn[db][collection]

str_2_list = lambda s : list(filter(None,(s.split("\n") if type(s) == str else [] )))

def insert_qna(table,question:str,multiplechoice:bool,option:str,answer:str,reference:str,explanation:str):
    # Check if question already exists ?
    doc = dict(
        question = str_2_list(question),
        multiplechoice = bool(multiplechoice),
        options = str_2_list(option),
        answer = str_2_list(answer),
        reference = str_2_list(reference),
        explanation = str_2_list(explanation)
    )
    ic(doc)
    query = dict(question = doc.get("question"))
    try:
        # Check if answers belongs to options
        if not set(doc.get("answer")).issubset(doc.get("options")):
            error_message = "Answer unavailable in options"
            raise AssertionError(error_message)

        # Check for existance
        if not table.count_documents(query):
            table.insert_one(doc)
            logger.info('Question Inserted')
            uuid = str(doc.pop("_id",None))
        
        else:
            logger.warning('Question already exists !')
            status = table.update_one(query,{"$set":{i:j for i,j in doc.items() if j not in [[],None,""]}})
            logger.info('Question Updated !')
            uuid = str(doc.pop("_id",None))
    except Exception as e:
        logger.error(e)
        return None

    return uuid

def get_qna(table):
    list_qna = []
    for i in table.find():
        i["_id"] = str(i["_id"])
        list_qna.append(i)
    return list_qna