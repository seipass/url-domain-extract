import argparse,csv,json,sys
def transform(value):
    from urllib.parse import urlsplit
    p=urlsplit(value if "://" in value else "//"+value)
    return (p.hostname or "").lower()

def main():
    parser=argparse.ArgumentParser(description='URL domain extractor')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    data=source
    result=transform(data)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
