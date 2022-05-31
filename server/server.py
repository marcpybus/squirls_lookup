#!/usr/bin/python3

import flask
import subprocess
import sys
import tempfile
import os
import shutil

squirls_data_hg19 = "/data_hg19"
squirls_data_hg38 = "/data_hg38"

app = flask.Flask(__name__)

@app.route('/squirls/<genome>/<database>/<variant_id>')
def run_squirls(database,genome,variant_id):

    if database in {"refseq","ensembl","ucsc"} and genome in {"hg19","hg38"}:

        if genome == "hg19":
            squirls_data = squirls_data_hg19
        else:
            squirls_data = squirls_data_hg38

        chromosome  = variant_id.split(":")[0]
        position  = variant_id.split(":")[1].split("-")[0]
        ref  = variant_id.split(":")[1].split("-")[1]
        alt  = variant_id.split(":")[1].split("-")[2]

        tempdir = tempfile.mkdtemp()
        with open(tempdir + "/input.vcf", 'w') as f:
            f.write("##fileformat=VCFv4.2\n")
            f.write("##FILTER=<ID=PASS,Description='All filters passed'>\n")
            f.write("##FORMAT=<ID=GT,Number=1,Type=String,Description='Genotype'>\n")
            f.write("##contig=<ID="+chromosome+",length=1000000000>\n")
            f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n")
            f.write(chromosome+"\t"+position+"\t.\t"+ref+"\t"+alt+"\t.\tPASS\t.\tGT\t1/0\n")
        
        print("running SQUIRLS.. please wait...")

        output = subprocess.call(["java", "-jar","/squirls/squirls-cli-2.0.0.jar","annotate-vcf","-d",squirls_data,"-f","html","-t",database.upper(),"--report-features","--all-transcripts",tempdir + "/input.vcf",tempdir + "/output"])

        html_file = open(tempdir + "/output.html", "r")
        html_text= html_file.read()
        html_file.close()

        shutil.rmtree(tempdir)

        if output == 0:
            return flask.render_template_string(html_text)   
        else:
            return "Something went wrong."
    else:
        return "ERROR! You must choose a correct genome (hg19 or hg38) and a correct database (refseq, ensembl or ucsc)"

if __name__ == '__main__':
    app.run(host ='0.0.0.0',debug=False)
    