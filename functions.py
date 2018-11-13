def get_s3_urls(data):
    message = data['Records'][0]['body']['Message']
    bucket = message['bucket']
    s3_input_file_paths = []
    s3_output_file_paths = []
    for i_file_path in message.get('inputFilePaths'):
        s3_input_file_paths.append('http://{}.s3.amazonaws.com/{}'.format(bucket, i_file_path))
    for o_file_path in message.get('outputFilePaths'):
        s3_output_file_paths.append('http://{}.s3.amazonaws.com/{}'.format(bucket, o_file_path))
    return s3_input_file_paths, s3_output_file_paths

def get_s3_reshift_urls(data):
    message = data['Records'][0]['body']['Message']
    bucket = message['bucket']
    s3_input_file_paths = []
    s3_output_file_paths = []
    for i_file_path in message.get('inputFilePaths'):
        s3_input_file_paths.append('s3://{}/{}'.format(bucket, i_file_path))
    for o_file_path in message.get('outputFilePaths'):
        s3_output_file_paths.append('s3://{}/{}'.format(bucket, o_file_path))
    return s3_input_file_paths, s3_output_file_paths


import psycopg2

def redshift(s3_url):
    "Requires psycopg2 package"

    conn = psycopg2.connect(dbname='**_dev_**', host='888888888888****.u.****.redshift.amazonaws.com', port='5439', user='******', password='********')
    cur = conn.cursor();

    //Begin your transaction
    cur.execute("begin;")

    cur.execute("copy kpi_kpireport from '{}' credentials 'aws_access_key_id=ID;aws_secret_access_key=KEY/KEY/pL/KEY' csv;".format(s3_url))
    ////Commit your transaction
    cur.execute("commit;")
    print("Copy executed fine!")
