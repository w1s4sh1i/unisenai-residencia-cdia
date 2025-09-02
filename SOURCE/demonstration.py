# [ ] send imports to .util.py
from util import *

# [x] Directory path
directory  = os.path.dirname(os.path.abspath(__file__))

# [x] Buid datapath -> dataset base
file_path = os.path.join(directory, '..', 'DATASET', 'bootcamp_train.csv')

# [x] Loading pandas DataFrame
df_train = pd.read_csv(file_path)

# [x] SQL Consulte (testing....)
# [ ] Update query
query = '''
SELECT
    "falha_maquina",
    COUNT(*) AS TotalDeFalhas
FROM
    df
GROUP BY
    "falha_maquina"
ORDER BY
    TotalDeFalhas DESC
'''

# Debugger

result = sqldf(query, locals())

# sys.stdout.write(result)