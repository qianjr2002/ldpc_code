import argparse
import ldpc_code
import numpy as np
# from pyldpc import encode
import ldpc_encode
import ldpc_decode


def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(
        description='Generate LDPC H and G matrices.')
    parser.add_argument('--n', type=int, default=8, help='码字长度，确保 d_c 能整除 n')
    parser.add_argument('--d_v', type=int, default=2, help='每列的 1 的个数')
    parser.add_argument('--d_c', type=int, default=4, help='每行的 1 的个数，必须整除 n')
    args = parser.parse_args()

    # 生成 H 和 G 矩阵
    H, G = ldpc_code.make_ldpc(args.n, args.d_v, args.d_c,
                               systematic=True, sparse=True)
    print("H Matrix:\n", H)
    print("G Matrix:\n", G)

    # 随机生成消息
    k = G.shape[1]  # 信息位长度
    message = np.random.randint(2, size=k)
    print("原始消息:\n", message)

    # 编码
    codeword = ldpc_encode.encode(G, message, snr=2)
    print("编码后的码字:\n", codeword)

    # 添加高斯噪声
    noise = np.random.normal(0, 1, codeword.shape)
    print("高斯噪声:\n", noise)
    received = codeword + noise
    print("接收到的信号:\n", received)

    # 解码
    decoded = ldpc_decode.decode(H, received, snr=2)
    decoded_message = ldpc_decode.get_message(G, decoded)
    print("解码后的消息:\n", decoded_message)

    # 验证消息一致性
    if np.array_equal(message, decoded_message):
        print("解码成功，消息一致！")
    else:
        print("解码失败，消息不一致！")


if __name__ == "__main__":
    main()
