### 1. Setting up your environment

Add the following environment variable to a `.env` file in the root directory of the project:
It is advised for all Python projects to setup a virtual environment specific to that project. To create a virtual environment, open your a terminal in an appropriate directory and run:

#### Windows
> ```
> python -m venv .env
> ```

This will create your virtual directory in a folder named `.env`.

Once you have the virtual environment created, you can activate it within your current terminal with the following command:  
#### Windows 
> ```
> .env\Scripts\activate
> ```

### 2. Install dependencies

pip install PyPDF2
pip install fitz 
pip install spacy