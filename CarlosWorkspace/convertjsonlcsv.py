import json
import csv

# Define paths for the input JSONL file and the output CSV file
input_file_path = 'sts-test.jsonl'
output_file_path = 'sts-test.csv'

# Open the output CSV file and set up the CSV writer
with open(output_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(['sentence 1', 'sentence 2', 'Response'])

    # Open and read the JSONL file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Parse each line (which is a JSON object) into a dictionary
            data = json.loads(line)
            
            # Extract the text block, then find and extract the required information
            text = data['text']
            # Extracting sentences and response
            try:
                sentence1_start = text.find('Sentence 1:') + len('Sentence 1:')
                sentence1_end = text.find('\nSentence 2:')
                sentence1 = text[sentence1_start:sentence1_end].strip()
                
                sentence2_start = text.find('Sentence 2:') + len('Sentence 2:')
                sentence2_end = text.find('\nAre they semantically similar?:')
                sentence2 = text[sentence2_start:sentence2_end].strip()
                
                response_start = text.find('Response:') + len('Response:')
                response = text[response_start:].strip()
                
                # Write the extracted data to the CSV file
                csv_writer.writerow([sentence1, sentence2, response])
            except Exception as e:
                print(f"Failed to process line: {line}")
                print(f"Error: {e}")
