from elements import elements  # Import the elements list from your module


def generate_element_html(element):
    # Use default values if the keys are missing in the element dictionary
    element = {**elements[element['atomic_number'] - 1], **element}

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{element['name']} - Element Details</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            .container {{
                background-color: #fff;
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            }}
            a {{
                text-decoration: none;
                color: #007BFF;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{element['name']} ({element['symbol']})</h1>
            <p>Atomic Number: {element['atomic_number']}</p>
            <p>Atomic Weight: {element['atomic_weight']}</p>
            <p>Electron Configuration: {element['electron_configuration']}</p>
            <p>Category: {element['category']}</p>
            <p>Standard State: {element['standard_state']}</p>
            <p>Boiling Point: {element['boiling_point']} K</p>
            <p>Melting Point: {element['melting_point']} K</p>
            <p>electron_configuration: {element['electron_configuration']}</p>
        </div>
    </body>
    </html>
    """
