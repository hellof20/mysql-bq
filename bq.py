from google.cloud import bigquery

def load_csv(file_path,table_id ):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=0, autodetect=False,
    )
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()

    table = client.get_table(table_id)  # Make an API request.
    return "Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id)