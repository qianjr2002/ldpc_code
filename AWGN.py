import numpy as np
import matplotlib.pyplot as plt


def plot():
    # 参数设置
    bandwidth = 1e6  # 信道带宽 (Hz)
    snr_db_range = np.arange(-10, 30, 1)  # 信噪比范围 (dB)

    # 将信噪比从分贝转换为线性值
    snr_linear = 10 ** (snr_db_range / 10)

    # 计算信道容量
    capacity = bandwidth * np.log2(1 + snr_linear)  # 单位: bits/s

    # 绘图
    plt.figure(figsize=(8, 6))
    plt.plot(snr_db_range, capacity / 1e6,
             label="AWGN Channel Capacity", color="b")
    plt.title("Channel Capacity vs. SNR (AWGN Channel)")
    plt.xlabel("SNR (dB)")
    plt.ylabel("Capacity (Mbps)")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
