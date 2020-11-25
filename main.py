from knowledge_base import KB
from sentence import Sentence
from utility import extract_keys
import sys, getopt


def main(argv):
    try:
        #':' mean need follow arg
        opts, _ = getopt.getopt(argv,"i:q:o:",["ifile=","queryfile=","ofile="])
    except getopt.GetoptError:
        print("Wrong syntax: python3 main.py -i <input prolog> -q <input query> -o <output file>")
        sys.exit(2)

    ifile = 'Lab02.pl'
    qfile = ''
    ofile = 'out.txt'
    kb = KB()
    queries = []
    
    for opt, arg in opts:
        if opt in ("-i","--ifile"):
            ifile = arg
            with open(ifile, 'r') as f_in:
                lines = f_in.readlines()
                for line in lines:
                    if "%" not in line and line.strip().replace("\n","") != "":
                        kb.add(line.replace(".", ""))

        elif opt in ("-q","--queryfile"):
            qfile = arg
            with open(qfile, 'r') as f_in:
                lines = f_in.readlines()
                for line in lines:
                    queries.append(line.replace(".", ""))

        elif opt in ("-o","--ofile"):
            ofile = arg
    
    with open(ofile, 'w') as f_out:
        for query in queries:
            q = Sentence(query, True)
            f_out.write("?- " + repr(q) + "\n")
            
            var_l = q.var_list
            result = kb.query(q)
            exported_result = set()
            
            for d in result:
                if d == {}:
                    f_out.write("True\n")
                    exported_result.add("True")
                    break
                res = extract_keys(d, var_l)
                res = tuple([repr(v) for _, v in res.items()])
                
                if res not in exported_result:
                    exported_result.add(res)
                    for var in var_l:
                        f_out.write(f"{var}: {repr(d[var])}\n")
                    if len(var_l)>1:
                        f_out.write("\n")
            
            if len(exported_result) == 0:
                f_out.write("False\n")
            f_out.write("\n")

if __name__ == "__main__":
    main(sys.argv[1:])