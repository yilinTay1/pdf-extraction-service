import json
import os

def export_to_file(data, file_path):
    """
    Export the extracted data to a JSON file.

    :param data: The data to export (should be in JSON serializable format)
    :param file_path: Path to the file where data should be saved
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write data to file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Data successfully exported to {file_path}")
    except Exception as e:
        print(f"Error exporting data to file: {e}")
