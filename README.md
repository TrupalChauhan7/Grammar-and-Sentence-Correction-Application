# Grammar and Sentence Correction Application

This is a Python-based application that utilizes OpenAI models to correct grammar and sentence structures. The project provides an easy-to-use GUI interface where users can input text, customize settings, and receive corrected output. This application is designed for students, professionals, and anyone looking for quick and accurate grammar corrections.

---

## Features

### 1. **User-Friendly Interface**
- Intuitive design built with PyQt6 for easy navigation and usage.

### 2. **Customizable OpenAI Parameters**
- **Max Tokens**: Adjust the number of tokens used in the response (minimum 10, maximum 4000).
- **Temperature**: Fine-tune the creativity of the response with adjustable temperature settings (0.0 to 1.0).

### 3. **Multi-Tab Functionality**
- Manage multiple grammar correction tasks simultaneously using tabs.

### 4. **Real-Time Grammar Correction**
- Input sentences or paragraphs in the text box and get immediate corrections powered by OpenAI models.

### 5. **Reset Functionality**
- Clear inputs and outputs with a single click to start fresh.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (you need to purchase or activate billing on OpenAI to generate an API key)

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Grammar-and-Sentence-Correction-Application.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Grammar-and-Sentence-Correction-Application
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Update your OpenAI API key in the `playground.py` file:
   ```python
   API_KEY = "your_openai_api_key_here"
   ```
6. Run the application:
   ```bash
   python app.py
   ```

---

## Screenshots
Include screenshots of the application showcasing:
1. The main interface with input/output fields.
2. Multi-tab functionality.
3. Settings for max tokens and temperature adjustments.

---

## Usage Notes
- To use OpenAI models, you need an active billing setup in your OpenAI account.
- Generate an API key from the OpenAI dashboard and replace the placeholder in `playground.py`.

---

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and create a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Ownership
This project is hosted on [Ishit Patel]'s GitHub account but was co-developed with [Trupal Chauhan].
This project was collaboratively created by:

- **Trupal Chauhan** ([GitHub Profile](https://github.com/TrupalChauhan7))
- **Ishit Patel** ([GitHub Profile](https://github.com/ishit-patel02))
