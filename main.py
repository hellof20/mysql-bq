import sql
import bq
import csv

file_path = 'deploy.csv'
table_id = "speedy-victory-336109.test.deploy"

db = sql.Database()
result = db.run_query("select * from deploy;")

with open(file_path, "w") as f:
    writer = csv.writer(f)
    writer.writerows(result)

bq.load_csv(file_path,table_id)