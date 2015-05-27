import sys,jinja2,yamli
def load_tmpl( tmpl_file=0, tmpl_dir=0 ):
    loader = jinja2.FileSystemLoader(tmpl_dir or '.')
    env = jinja2.Environment(loader=loader)
    return env.get_template(tmpl_file or sys.stdin)
def main( tmpl_name, data_name=None ):
    data = yamli.load( open(data_name) ) \
        if data_name else {}
    print load_tmpl( tmpl_name ).render( **data )
    pass
if __name__=='__main__': main( *sys.argv )
