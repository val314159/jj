import sys,jinja2,yamli
def main( tmpl_text, data_text ):
    data = yamli.load( data_text )
    tmpl = jinja2.Template( tmpl_text ).
    f_out.write( tmpl.render( ** data ) )
if __name__=='__main__': main( *sys.argv )
