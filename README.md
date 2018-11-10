# SwetaPyProj

1. Read message.json
2. Parse "body" --> "message" in specific
		tId
		vId
		projut
		calendarDate
		factS
		sId
		jagya
		bucket
		inputFilePaths
			input-files/tId=1600000/vId=430000/sinput/file1.csv (example)
			....
			
		outputFilePaths
			output-files/tId=1600000/vId=430000/soutput/ofile1.txt (example)
			....
		isValid
		receivedTimestamp
3. load fields in 2) in a test_table in redshift.
4. bucket and inputFilePaths and outputFilePaths provide S3 file path where files reside. 
5. Load files to redshift. so if 5 input files and 4 output files then total of 5+4 = 9 tables. table structure (anything sample col1 , col2 col3)
		