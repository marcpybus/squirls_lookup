
## squirls_lookup: A look up server for SQUIRLS 2.0

This application functions as an online & easy look up server for Squirls software.  
It can be installed via Docker Compose (tested on Ubuntu 18.04 / 20.04 ).  

* you need to configure Docker and Docker Compose before installing this package

### Configuration

1. Clone this repository:

`$ git clone git@github.com:marcpybus/squirls_lookup.git`

2. Download reference data for hg19 and/or hg38 and extract them in the main directory:

> 2203	hg19/GRCh37	~11.9 GB unpacked  
> 2203	hg38/GRCh38	~12.2 GB unpacked  

`$ cd squirls_lookup`  
`$ wget https://storage.googleapis.com/squirls/2203_hg19.zip`  
`$ wget https://storage.googleapis.com/squirls/2203_hg39.zip`  
`$ unzip 2203_hg19.zip -d 2203_hg19`  
`$ unzip 2203_hg38.zip -d 2203_hg38`  

3. Build & start the server on default port (5000):

`$ docker-compose -f squirls_lookup.yml build`  
`$ docker-compose -f squirls_lookup.yml up -d`  

4. Stop the server using:

`$ docker-compose -f squirls_lookup.yml down`  

5. Modifiy the server port by changing this parameter at `squirls_lookup.yml`:

> ports:  
> &emsp;&emsp;\-"5000:80" -> HOST:CONTAINER  

6. To check out a given genomic variant, open a broswer and type:

	``http://<HOST>:<PORT>/squirls/<GENOME>/<DB>/<VARIANT_ID>``

## Examples 
	
> http://localhost:5000/squirls/hg19/refseq/chr16:2166832-A-G  
> http://192.168.103.120:5000/squirls/hg19/ensembl/chr16:2166832-A-G  
> http://192.168.103.112:5000/squirls/hg19/ucsc/chr16:2166832-A-G  

* you can choose among refseq, ensembl or ucsc databases and between genome versions hg19 or hg38
