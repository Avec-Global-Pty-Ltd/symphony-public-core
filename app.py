## Front end
import streamlit as st

## Paths
from pathlib import Path
import os
import sys
file_path = Path(__file__).resolve().parent

## Initial startup - logging, credentials, config
if 'logger' not in st.session_state: # startup
    import logging # confirm if this goes in or out of the loop

    if os.getenv("WEBSITE_RESOURCE_GROUP") is not None: # Azure

        ## Logging
        logger = logging.getLogger("azure.mgmt.resource")
        handler = logging.StreamHandler(stream=sys.stdout)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.info("using Azure logger")

    else: # local

        ## Logging
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='w')
        for spam in ['PIL', 'openai', 'httpcore', 'azure', 'urllib3', 'httpx']:
            logging.getLogger(spam).setLevel(logging.WARNING)
        logger.info("using local logger")

    st.session_state.logger = logger
else: # UI refresh
    logger = st.session_state.logger

if st.button("List all files"):
    # Recursively list all files with their full paths
    for file in Path.cwd().rglob('*'):
        if file.is_file():
            logger.info(file)
            st.write(file)