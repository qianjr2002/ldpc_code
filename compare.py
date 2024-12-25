import numpy as np
import matplotlib.pyplot as plt
import shared_rate


def simulate_ldpc_performance(snr_db_range, fixed_rate=True):
    adaptive_rate = shared_rate.rate_LDPC
    ber_results = []
    for snr_db in snr_db_range:
        snr_linear = 10 ** (snr_db / 10)
        # 固定编码方案: 码率固定
        if fixed_rate:
            rate = 0.5  # 假设固定码率为1/2
        else:
            # 自适应编码方案: 码率根据SNR调整
            rate = adaptive_rate
        # 模拟BER (根据实际情况用LDPC编码计算误码率)
        ber = 0.5 / (1 + snr_linear * rate)  # 示例公式
        ber_results.append(ber)
    return ber_results


def compare():
    # 设置信噪比范围
    snr_db_range = np.arange(-5, 20, 1)

    # 模拟固定和自适应编码性能
    ber_fixed = simulate_ldpc_performance(snr_db_range, fixed_rate=True)
    ber_adaptive = simulate_ldpc_performance(snr_db_range, fixed_rate=False)

    # 绘制性能曲线
    plt.figure(figsize=(10, 6))
    plt.semilogy(snr_db_range, ber_fixed,
                 label="Fixed Coding (Rate=1/2)", linestyle="--")
    plt.semilogy(snr_db_range, ber_adaptive,
                 label="Adaptive Coding", linestyle="-")
    plt.title("BER Performance: Fixed vs Adaptive Coding")
    plt.xlabel("SNR (dB)")
    plt.ylabel("BER (log scale)")
    plt.grid(True, which="both")
    plt.legend()
    plt.show()


def main():
    compare()


if __name__ == "__main__":
    main()
