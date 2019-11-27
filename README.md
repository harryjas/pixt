# Pixt #
Pixt is an application that let's you upload, store, and play all of your music from the cloud. You can now manage and listen to your music from any device, anywhere in the world.

## Setting up your Development Environment ##
1. First, fork this repository to your account.

2. Create a virtual environment on your machine. 
    ```
    virtualenv env
    ```
    We recommend using python-virtualenv. Any other packages would do fine though.

3. Activate the newly created virtual env:
    ```
    cd env
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/harryjas/pixt.git
    ```
    
5. Install the dependencies for the project.
    ```
    cd pixt
    pip3 install -r requirements.txt
    ```
    
6. Run the migrations and collect staticfiles
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    
7. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    Once the server is started, open http://127.0.0.1:8000 in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.
