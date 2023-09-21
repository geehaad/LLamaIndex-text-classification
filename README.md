<h1>G-Text Classifier using LLamaIndex and Gradio📋</h1>

<p>Welcome to G-Text Classifier, a powerful tool for classifying text based on user-defined labels.<b> Make text classification a breeze! 😎</b>
</p>

<h2>Table of Contents</h2>
<ul>
<li>Overview
<li>Features
<li>Getting Started
<li>Usage
<li>Contributing
</ul>

<h2>Overview</h2>
<pre>
G-Text Classifier is a user-friendly application that takes a piece of text or a file and classifies it based on the label provided by the user. Whether you're analyzing sentiment, categorizing documents, or any other text classification task, this tool has you covered.
Here we used GPT from LlamaIndex beside Gradio open-source Python package to build fast UI components.
</pre>
<h2>Interface 🎨</h2>
<img src = "img/txt.png">
<img src = "img/file.png">
<h2>Code Structure</h2>

<h3>The project is organized as follows:</h3>
<pre>
Text_classification/
|-- data/: This directory contains the data used for text classification.
| |-- Reviews.csv: Sample CSV data for classification (if applicable).
| |-- reviews.txt: Sample text data for classification (if applicable).

|-- prototype/: This directory holds the prototype code.
| |--webApp.py: The main Python script for the Gradio web application.

|-- src/: This directory contains the project source code.
| |-- components/: Subdirectory with essential components for text classification.
| | |-- __init__.py: Initialization file for the components directory.
| | |-- helper.py: Helper functions for text classification.

|-- storage/: This directory stores the output of indexing the data for efficient classification.
| |-- docstore.json: Document store file.
| |-- graph_store.json: Graph store file.
| |-- index_store.json: Index store file.
| |-- vector_store.json: Vector store file.

|-- README.md: This file, providing an overview of the project and its structure.
</pre>

<h2>Features</h2>
✨ Text Classifier comes with the following features:

📄 Text Classification: Enter plain text along with a label and get instant classification results.
📁 File Upload: Upload text files for batch classification.
🌟 User-Friendly Interface: Built with Gradio for an intuitive and interactive user experience.

<h2>Getting Started</h2>

👨‍💻 To get started with Text Classifier, follow these simple steps:
<ol>
<li>
Clone the repository:

```bash
git clone https://github.com/geehaad/LLamaIndex-Text-Classification.git
cd LLamaIndex-Text-Classification
```
<li>
Install the required dependencies:

```bash
pip install -r requirements.txt
```
<li>
Start the application (you can run the helper file to get the output in your terminal, or use the interface):

```bash
python helper.py
python prototype/webApp.py
```
<li>
Access the application in your browser at http://localhost:5000. (the linke will appear in your terminal)

</ol>

<h2>Usage</h2>

<h3>🚀 Using the Text Classifier with Gradio is easy and user-friendly. You have two options:</h3>
<h4>Text Classification</h4>
<ol>
<li>Select the "Text" tab to classify individual text entries.
<li>Enter the text in the "context" textbox.
<li>Specify how you want to classify it in the "Labels" textbox.

<li>Click "Get Classification" to see the result.
</ol>
<h4>File Classification</h4>
<ol>
<li>Select the "Files" tab to classify text from a file.
<li>Upload a text file using the "context" file input.
<li>Specify the classification labels in the "Labels" textbox.
<li>Click "Get Classification" to process the file and view the results.
</ol>

<h3>Helper File (helper.py)</h3>
The helper.py file in the src/components directory contains the essential functions for text classification. It uses OpenAI's GPT model for classification.

<h4>Here's a brief overview of the helper functions:</h4>

<code>analyze_file(file_path, labels): </code>Classifies text from a file based on provided labels.<br>
<code>analyze_text(text, labels): </code>Classifies a single text entry based on provided labels.<br>

<b>To use the helper functions, ensure that your OpenAI API key is set correctly in helper.py.<b>

<h2>Contributing</h2>
🤝 We welcome contributions from the community to make Text Classifier even better. If you'd like to contribute, please follow these guidelines:
<ul>
<li>
Fork the repository.
<li>
Create a new branch:

```bash
git checkout -b feature/your-feature-name. 
```

<li>
Make your changes and commit them: 

```bash
git commit -m 'Add some feature'.
```
<li>
Push to your branch:

```bash 
git push origin feature/your-feature-name.
```
<li>
Create a pull request.
</ul>

Start classifying text like a pro with Text Classifier. Whether it's sentiment analysis, document categorization, or any other text classification task, we've got you covered. If you have any questions or suggestions, feel free to reach out. Happy classifying! 📋🚀<br>

To know more about LlamaIndex: <a href=https://www.llamaindex.ai/>llamaindex.ai</a>
