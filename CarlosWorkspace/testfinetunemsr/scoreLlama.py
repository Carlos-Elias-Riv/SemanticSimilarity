import json
import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


file_path = "output.jsonl"
results = []
pattern = r'[a-zA-Z]+'
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Convert the JSON string to a dictionary
        #print(line)
        data = json.loads(line)
        # Append the dictionary to the list
        #data_list.append(data)
        pos = data['text'].find("Response:")
        data['text'] = data['text'][pos + len("Response:"):]
        data['text'] = data['text'].replace(" ", "")
        matches  = re.findall(pattern, data['text'])
        
        text = ""

        for match in matches:
            text += match

        data['text'] = text
        results.append(data)

#print(results)
        
ground_truth = []

with open("test.jsonl", 'r') as file:
    for line in file:
        data = json.loads(line)
        pos = data['text'].find("Response:")
        data['text'] = data['text'][pos + len("Response:"):]
        data['text'] = data['text'].replace(" ", "")
        ground_truth.append(data)

#print(ground_truth)
possible_answers = ['yes', 'no']
matchcounter = 0
errorcounter = 0

final_truth = []
final_results = []

for pos in range(len(ground_truth)):
    print(ground_truth[pos]['text'], results[pos]['text']) 
    if results[pos]['text'] in possible_answers:
        if ground_truth[pos]['text'] == results[pos]['text']:
            print("Match")
            matchcounter += 1
        else:
            print("No match")

        if ground_truth[pos]['text'] == "yes":
            final_truth.append(1)
        else: 
            final_truth.append(0)
        
        if results[pos]['text'] == "yes":
            final_results.append(1)
        else: 
            final_results.append(0)

    else: 
        print("Error")
        errorcounter += 1

print("Match counter: ", matchcounter)
print("Error counter: ", errorcounter)
print("Len ground_truth", len(ground_truth))

def get_scores(target_output, similarities):

    
    #print("Confusion Matrix:")
    #print(conf_matrix)
    #disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['No', 'Yes'])
    #disp.plot(cmap=plt.cm.Blues)
    #plt.title(title)
    #plt.show()

    # Calculate precision, recall, and F1-score
    precision = precision_score(target_output, similarities)
    recall = recall_score(target_output, similarities)
    f1 = f1_score(target_output, similarities)
    acc_score = accuracy_score(target_output, similarities)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Accuracy Score: {acc_score:.2f}")
    print("#####")

get_scores(final_truth, final_results)