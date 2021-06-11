from flask import Flask, request, escape
from flask import render_template, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def hello():
    sContent = '''<!DOCTYPE html
    <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            
            <style>
                h1 {
                    border: 2px #eee solid;
                    color: brown;
                    text-align: center;
                    padding: 10px;
                }
            </style>
        <meta charset="UTF-8">
        
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        
        <title>S2.Security - SSH Banner to OS Version Lookup - v0.0.5</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <a class="navbar-brand" href="https://S2.Security">S2.Security</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">About</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
        
            <h1>SSH Banner to OS Version - Lookup</h1>
    
            <form action="/dev005/greet" method="get">
                <div class="form-group">
                    <label for="title">SSH Banner (e.g. nc ip.ip.ip.ip 22 -> SSH Banner)</label>
                    <input type="text" name="name"
                           placeholder="Post title" class="form-control"
                           value="SSH-2.0-OpenSSH_7.4"></input>
                </div>
            

                <div class="form-group">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        
        
    
    

        </body>
    </html>
    '''
    
    '''
                    <div class="form-group">
                    <label for="content">Content</label>
                    <textarea name="content" placeholder="Post content"
                              class="form-control">bbbtestbbb</textarea>
                </div>
    '''
    
    return sContent #return render_template('index.html') # return 'Hello, World!'

@app.route('/greet')
def greet():
    rawInputName = request.args['name']
    strippedRawInputName = rawInputName.strip()
    escapeStrippedRawInputName = escape(strippedRawInputName)
    # nc 54.177.123.107 22
    myListOfSshBanners = [
    	{
    	    # Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-0b2ca94b5b49e0132 (64-bit x86) / ami-00d59b32715507cba (64-bit Arm)
    		'banner':'SSH-2.0-OpenSSH_7.4',
    		'os':'Amazon Linux 2',
    		'arch':'64-bit x86',
    		'ami':'ami-0b2ca94b5b49e0132',
    		'etc_release':'''NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"
Amazon Linux release 2 (Karoo)
cpe:2.3:o:amazon:amazon_linux:2'''
    	},
    	{
    	    # Red Hat Enterprise Linux 8 (HVM), SSD Volume Type - ami-054965c6cd7c6e462 (64-bit x86) / ami-05f88a4bcb91f4ea7 (64-bit Arm)
            'banner':'SSH-2.0-OpenSSH_8.0',
    		'os':'Red Hat Enterprise Linux 8',
    		'arch':'64-bit x86',
    		'ami':'ami-054965c6cd7c6e462',
    		'etc_release':'''NAME="Red Hat Enterprise Linux"
VERSION="8.4 (Ootpa)"
ID="rhel"
ID_LIKE="fedora"
VERSION_ID="8.4"
PLATFORM_ID="platform:el8"
PRETTY_NAME="Red Hat Enterprise Linux 8.4 (Ootpa)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:redhat:enterprise_linux:8.4:GA"
HOME_URL="https://www.redhat.com/"
DOCUMENTATION_URL="https://access.redhat.com/documentation/red_hat_enterprise_linux/8/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"

REDHAT_BUGZILLA_PRODUCT="Red Hat Enterprise Linux 8"
REDHAT_BUGZILLA_PRODUCT_VERSION=8.4
REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux"
REDHAT_SUPPORT_PRODUCT_VERSION="8.4"
Red Hat Enterprise Linux release 8.4 (Ootpa)
Red Hat Enterprise Linux release 8.4 (Ootpa)
cpe:/o:redhat:enterprise_linux:8.4:ga'''
    	},
    	{
    		# SUSE Linux Enterprise Server 15 SP2 (HVM), SSD Volume Type - ami-05c558c169cfe8d99 (64-bit x86) / ami-05e206de142efa13a (64-bit Arm)
            'banner':'SSH-2.0-OpenSSH_8.1',
    		'os':'SUSE Linux Enterprise Server 15 SP2',
    		'arch':'64-bit x86',
    		'ami':'ami-05c558c169cfe8d99',
    		'etc_release':'''NAME="SLES"
VERSION="15-SP2"
VERSION_ID="15.2"
PRETTY_NAME="SUSE Linux Enterprise Server 15 SP2"
ID="sles"
ID_LIKE="suse"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:suse:sles:15:sp2"'''
    	}
    ]
    # https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
    lMatch = list(filter(lambda person: person['banner'] == strippedRawInputName, myListOfSshBanners))
    
    if len(lMatch) <= 0:
        lMatch = [{'banner':strippedRawInputName,
    		'os':'???',
    		'arch':'???',
    		'ami':'???',
    		'etc_release':'''???'''}]
    
        sOutput = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Search Results</h1>
        <pre>
OS: {0}
        
Arch: {1}
        
AMI: {2}
        
/etc/*release*: 

{3}

###
        </pre>
    </body>
    </html>'''.format(lMatch[0]["os"], lMatch[0]["arch"], lMatch[0]["ami"], lMatch[0]["etc_release"]) # .format(escape(lMatch[0]["os"]))
    
    
    sOutputTwo = '''
        <pre>
OS: {0}
        
Arch: {1}
        
AMI: {2}
        
/etc/*release*: 

{3}

###
        </pre>
        '''.format(lMatch[0]["os"], lMatch[0]["arch"], lMatch[0]["ami"], lMatch[0]["etc_release"]) # .format(escape(lMatch[0]["os"]))
    
    sContent = '''<!DOCTYPE html
    <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            
            <style>
                h1 {
                    border: 2px #eee solid;
                    color: brown;
                    text-align: center;
                    padding: 10px;
                }
            </style>
        <meta charset="UTF-8">
        
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        
        <title>S2.Security - SSH Banner to OS Version Lookup - v0.0.5</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <a class="navbar-brand" href="https://S2.Security">S2.Security</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">About</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
        
            <h1>SSH Banner to OS Version - Search Results</h1>
    
            <form action="/dev005/greet" method="get">
                <div class="form-group">
                    '''+sOutputTwo+'''
                </div>
            </form>
        
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        
        
    
    

        </body>
    </html>
    '''
    
    return sContent
