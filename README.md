# finalYearProject

[comment]: <> (## Author)

[comment]: <> (- [Nadeem Abdelkader]&#40;https://github.com/Nadeem-Abdelkader&#41;)

[comment]: <> (## What Is This?)

## Set Up and Run

1. Download and install Python 3.10 from <https://www.python.org/downloads/> and make sure to add Python to PATH if you are using Windows

2. Clone or download the git repository
   [here](https://github.com/Nadeem-Abdelkader/finalYearProject.git).
    ```sh
    git clone https://github.com/Nadeem-Abdelkader/finalYearProject.git
    ```

3. Navigate to the cloned local repository
    ```sh
    cd finalYearProject
    ```

4. Create a new virtual environment
   
   MacOS and Linux
   ```sh
   pip install pipenv
   ```
   Windows
   ```sh
   pip3 install pipenv
   ```
   
5. Navigate to the project folder
    ```sh
    cd finalyearproject
    ```
    
6. Activate the new virtual environment
    ```sh
   pipenv shell
   ```

7. Install required dependencies 
    ```sh
   pip install -r ../requirements.txt
   ```
   
8. Make migrations
    ```sh
   python3 manage.py makemigrations
   ```
   
9. Apply migrations
    ```sh
   python3 manage.py migrate
   ```

10. Start the applciation
    ```sh
    python3 manage.py runserver
    ```
11. Navigate to localhost
   - Visit http://127.0.0.1:8000/
