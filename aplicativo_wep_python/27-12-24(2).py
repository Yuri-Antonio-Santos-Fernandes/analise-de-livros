import sys
from streamlit .web import cli as stcli

sys.argv = ["streamli", "run", "27-12-24.py"]
sys.exit(stcli.main())

#executor do app web
#o inicialize primeiro