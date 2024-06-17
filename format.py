import pandas as pd
import jsonlines
import sys
import os

def df_to_jsonl_string(df):
    """
    Converts a DataFrame to a JSONL formatted string.
    """
    for index, row in df.iterrows():
      try:
        prompt = f"You are an expert in answering questions based on provided evidence. Answer the given question using the following context. Question: {row['Question']}\nContext:{row['ChunkTexts']}"
            completion = f"Here is my answer: {row['Answer']}\nHere is the ID of the text I used to answer the question: {str(row['Quoted_Text_ID'])}"
            output.append({"prompt": prompt, "completion": completion})
        except Exception as e:
            print(f"Error processing row {index}: {e}")
    return output


def main():
    # Check if the user provided a CSV file path as an argument
    if len(sys.argv) < 2:
        print("Please provide the path to the CSV file as an argument.")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    if not os.path.exists(csv_file_path):
        print(f"File {csv_file_path} does not exist!")
        sys.exit(1)

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

    # Check if the DataFrame has the required columns
    required_columns = [
        'ChunkIDs', 'ChunkTexts', 'Question', 'Answer', 'Quoted_Text_ID'
    ]
    if not all(column in df.columns for column in required_columns):
        print("Invalid file format! The CSV file must contain the columns: 'ChunkIDs', 'ChunkTexts', 'Question', 'Answer', 'Quoted_Text_ID'")
        sys.exit(1)

    # Convert the DataFrame to JSONL format
    jsonl_output = df_to_jsonl_string(df)

    # Write the JSONL content to a file
    output_file_path = os.path.splitext(csv_file_path)[0] + "_output.jsonl"
    try:
        with jsonlines.open(output_file_path, mode='w') as writer:
            writer.write_all(jsonl_output)
    except Exception as e:
        print(f"Error writing to JSONL file: {e}")
        sys.exit(1)

    print(f"JSONL file saved to {output_file_path}")


if __name__ == "__main__":
    main()
