# Instagram Comments Scraper and data process

1. Create Virtual Environment (Recommended)<br/> 
    - `pip install virtualenv`
    - `virtualenv .venv`  
    
2. Activate the virtual environment
    - `source .venv/bin/activate`

3. Install dependencies
    - `pip install -r requirements.txt`

4. Install Chrome Web Driver
    - `wget https://chromedriver.storage.googleapis.com/x.xx/chromedriver_linux64.zip` <br>
    See the latest Chrome web driver on https://sites.google.com/a/chromium.org/chromedriver/downloads <br /> <br />
    - Extract and move the binary to bin: `.venv/bin/`
    - Make it executable `chmod +x .venv/bin/chromedriver`

5. Run 
    - `python scraper.py`
 
6. Deactivate the virtual environment
    - `deactivate`
