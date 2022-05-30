
THE LOOK UP SERVER FOR SQUIRLS version 1

This application 


SETTING UP & RUNNING 

1. Clone this repository where ever you want:

	git clone marcpybus

2. Download reference data for hg19 and/or hg38 and extract it in the main directory

2203	hg19/GRCh37	https://storage.googleapis.com/squirls/2203_hg19.zip	~9.5 GB for download, ~11.9 GB unpacked
2203	hg38/GRCh38	https://storage.googleapis.com/squirls/2203_hg38.zip	~9.9 GB for download, ~12.2 GB unpacked

3. Build & start the server on port 5000:

docker-compose -f squirls_lookup.yml build
docker-compose -f squirls_lookup.yml up

4. Modify "squirls_lookup.yml" file to change the used port

    ports:
      - "5000:80" -> HOST:CONTAINER


