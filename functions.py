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
