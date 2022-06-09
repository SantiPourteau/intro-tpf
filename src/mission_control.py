import argparse

def run(path_partitura: str, path_instrumento:str) -> None:
    print(path_instrumento)
    print(path_partitura)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('a',type=str, help='el path a una partitura')
    parser.add_argument('b',type=str, help='el path a una partitura')
    parser.add_argument('c',type=str, help='el path a una partitura')
    args = parser.parse_args()
    run(args.p)
