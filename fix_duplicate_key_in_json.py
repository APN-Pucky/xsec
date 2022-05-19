import json
import sys 

def myhook(pairs):
    d = {}
    for k, v in pairs:
        if k not in d:
          d[k] = v
        else:
          d[k] = {**d[k],**v} 
    return d

def main(argv):
    for f in argv[1:]:
        mydata = json.load(open(f), object_pairs_hook=myhook)
        open(f,'w').write( json.dumps(mydata))

if __name__ == "__main__":
    main(sys.argv)
