import json
import csv
import requests
import security as sec
import json 

question = "clase"

def get_score (question, filter_query = ""):

    result = sec.discovery.query(
                    environment_id=sec.environment_id, 
                    collection_id=sec.collection_id, 
                    deduplicate=False, 
                    highlight=True, 
                    passages=True, 
                    passages_count=5,
                    filter = filter_query,
                    natural_language_query=question, 
                    count=5
                    )

    result = result.get_result()['results']
    total_score = 0

    for res in result:
        tmp = res['result_metadata']
        #print(tmp)
        total_score += float(tmp['score'])

    return total_score

print(get_score(question, "abstracta"))


'''
output_file = open("./training_file.tsv", "w")
writer = csv.writer(output_file, delimiter="\t")
try:
    with open ("./Questions.txt", encoding="Windows 1252") as questions:
        noOfQuestions = 0
        for line in questions:
            print("Question No = " + str(noOfQuestions + 1))
            question = line.replace("\n", "")
            print("Question = " + question)

            question = "%s" % (question)

            #run Discovery query to get results from untrained service 
            #print("Query Response = " + json.dumps(result.get_result()))

            #create a row for each query and results 
            result_list = [question]
            for resultDoc in result.get_result()["results"]:
                id = resultDoc["id"]
                text = resultDoc["text"]
            #for resultDoc in result.get_result()["passages"]:
                #id = resultDoc["document_id"]
                #text = resultDoc["passage_text"]
                if( len(text) > 1000 ):
                    text = text[:1000] 
                result_list.extend([id,text,' ']) #leave a space to enter a relevance label for each doc 

            #write the row to the file 
            writer.writerow(result_list)
            noOfQuestions = noOfQuestions + 1
            print("==========================================================")
            print("")
    print("tsv file with questions and query results created")
    print("Number of questions processed = " + str(noOfQuestions))
    output_file.close()
except Exception as e:
    print("Exception occurred ####### ")
    print(e)
'''
