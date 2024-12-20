import argparse
import ldpc_code


def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(
        description='Generate LDPC H and G matrices.')
    parser.add_argument('--n', type=int, default=8, help='码字长度，确保 d_c 能整除 n')
    parser.add_argument('--d_v', type=int, default=2, help='每列的 1 的个数')
    parser.add_argument('--d_c', type=int, default=4, help='每行的 1 的个数，必须整除 n')
    args = parser.parse_args()

    # 生成 H 和 G 矩阵
    H, G = ldpc_code.make_ldpc(
        args.n, args.d_v, args.d_c, systematic=True, sparse=True)
    print("H Matrix:\n", H)
    print("G Matrix:\n", G)


if __name__ == "__main__":
    main()
