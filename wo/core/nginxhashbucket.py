"""WordOps Hash Bucket Calculator"""
import fileinput
import math
import os
import subprocess

from wo.core.fileutils import WOFileUtils


def hashbucket(self):
    # Check Nginx Hashbucket error
    sub = subprocess.Popen('nginx -t', stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, shell=True)
    output, error_output = sub.communicate()
    if 'server_names_hash_bucket_size' not in str(error_output):
        return True

    count = 0
    # Get the list of sites-availble
    sites_list = os.listdir("/etc/nginx/sites-enabled/")

    # Count the number of characters in site names
    for site in sites_list:
        count = sum([count, len(site)])

    # Calculate Nginx hash bucket size
    ngx_calc = math.trunc(sum([math.log(count, 2), 2]))
    ngx_hash = math.trunc(math.pow(2, ngx_calc))

    # Replace hashbucket in Nginx.conf file
    if WOFileUtils.grepcheck(self, "/etc/nginx/nginx.conf",
                             "# server_names_hash_bucket_size 64;"):
        ngxconf = open("/etc/nginx/conf.d/hashbucket.conf",
                       encoding='utf-8', mode='w')
        ngxconf.write("\tserver_names_hash_bucket_size {0};".format(ngx_hash))
        ngxconf.close()
    elif WOFileUtils.grepcheck(self, "/etc/nginx/nginx/conf",
                               "server_names_hash_bucket_size"):
        for line in fileinput.FileInput("/etc/nginx/nginx.conf", inplace=1):
            if "server_names_hash_bucket_size" in line:
                print("\tserver_names_hash_bucket_size {0};".format(ngx_hash))
            else:
                print(line, end='')

    else:
        ngxconf = open("/etc/nginx/conf.d/hashbucket.conf",
                       encoding='utf-8', mode='w')
        ngxconf.write("\tserver_names_hash_bucket_size {0};".format(ngx_hash))
        ngxconf.close()
