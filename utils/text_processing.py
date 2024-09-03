def associate_labels_with_fields(fields, labels):
    extracted_data = []

    for field in fields:
        field_name = field['name']
        field_value = field['value']
        field_page = field['page']
        field_rect = field['rect']

        # Find label closest to field based on some heuristic (e.g., proximity, position)
        associated_label = None
        min_distance = float('inf')
        for label in labels:
            if label['page'] == field_page:
                label_text = label['text']
                # Simple heuristic: distance calculation
                distance = calculate_distance(field_rect, label_text)
                if distance < min_distance:
                    min_distance = distance
                    associated_label = label_text

        extracted_data.append({
            'field_name': field_name,
            'value': field_value,
            'label': associated_label.strip() if associated_label else 'Unknown'
        })

    return extracted_data

def calculate_distance(field_rect, label_text):
    # Implement a function that calculates the distance between field and label
    # Use coordinates and spatial analysis to compute proximity
    # Placeholder for distance calculation logic
    return 0
