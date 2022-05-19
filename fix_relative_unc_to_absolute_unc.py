import json
import sys 

def recursive_for_replace(data):
    if "xsec_pb" in data and "unc_pb" in data:
        data["unc_pb"] = data["unc_pb"] * data["xsec_pb"]
        return
    for k in data:
        recursive_for_replace(data[k])

def main(argv):
    for f in argv[1:]:
        mydata = json.load(open(f))

        recursive_for_replace(mydata["data"])

        open(f ,'w').write( json.dumps(mydata))

if __name__ == "__main__":
    main(sys.argv)

